"""REST API for CareerGuide AI. Run with: uvicorn api:app --reload"""
from typing import Dict, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from assessment import SKILL_LABELS, BRANCH_SKILL_LABELS, get_adaptive_questions, get_difficulty, calculate_skill_scores
from recommendation import recommend_careers, get_career_match_details
from skill_gap import analyze_skill_gap
from roadmap import generate_roadmap

app = FastAPI(title="CareerGuide AI API", description="API for adaptive skill assessment, career recommendations, skill-gap analysis, and learning roadmaps.", version="1.0.0")

class QuestionsRequest(BaseModel):
    self_ratings: Dict[str, int]
    branch: str = "CSE"
    semester: int = Field(default=1, ge=1, le=8)

class AnswerItem(BaseModel):
    skill: str
    question_id: int = Field(ge=0)
    selected_option: str

class ScoreRequest(BaseModel):
    self_ratings: Dict[str, int]
    responses: List[AnswerItem]
    branch: str = "CSE"
    semester: int = Field(default=1, ge=1, le=8)

class ProfileRequest(BaseModel):
    name: str = "Student"
    branch: str = "CSE"
    semester: str = "7th"
    skill_scores: Dict[str, float]

class CareerRequest(ProfileRequest):
    top_n: int = Field(default=3, ge=1, le=10)

class SkillGapRequest(ProfileRequest):
    career: str

def validate_ratings(ratings, branch="CSE"):
    branch = branch.upper()

    if branch not in BRANCH_SKILL_LABELS:
        raise HTTPException(
            status_code=422,
            detail="Branch must be CSE, ISE, or ECE."
        )

    expected_skills = BRANCH_SKILL_LABELS[branch]

    missing = [
        skill for skill in expected_skills
        if skill not in ratings
    ]

    extra = [
        skill for skill in ratings
        if skill not in expected_skills
    ]

    if missing or extra:
        raise HTTPException(
            status_code=422,
            detail={
                "message": "Provide ratings for exactly the skills required by your branch.",
                "missing_skills": missing,
                "unexpected_skills": extra,
            },
        )

    invalid = {
        skill: value
        for skill, value in ratings.items()
        if (
            not isinstance(value, int)
            or isinstance(value, bool)
            or not 1 <= value <= 5
        )
    }

    if invalid:
        raise HTTPException(
            status_code=422,
            detail={
                "message": "Confidence ratings must be integers from 1 to 5.",
                "invalid_ratings": invalid,
            },
        )

def build_profile(payload):
    branch = payload.branch.strip().upper()

    if branch not in BRANCH_SKILL_LABELS:
        raise HTTPException(
            status_code=422,
            detail="Branch must be CSE, ISE, or ECE."
        )

    active_skills = BRANCH_SKILL_LABELS[branch]
    unknown = [
        skill for skill in payload.skill_scores
        if skill not in active_skills
    ]

    if unknown:
        raise HTTPException(
            status_code=422,
            detail={
                "message": "Unknown skill name(s) for this branch.",
                "unknown_skills": unknown
            }
        )

    scores = {}
    for skill in active_skills:
        score = float(payload.skill_scores.get(skill, 0))
        if not 0 <= score <= 100:
            raise HTTPException(
                status_code=422,
                detail=f"Score for '{skill}' must be between 0 and 100."
            )
        scores[skill] = score

    return {
        "name": payload.name,
        "branch": branch,
        "semester": payload.semester,
        "skills": [
            skill for skill, score in scores.items()
            if score >= 60
        ],
        "skill_scores": scores
    }
def enrich_gap(gap, details):
    rows = gap.get("skill_rows", details.get("skill_rows", []))
    gap["skill_rows"] = rows
    gap.setdefault("coverage", details.get("match_score", 0))
    gap.setdefault("matched_skills", [r["skill"] for r in rows if r.get("current_score", 0) >= r.get("required_score", 70)])
    gap.setdefault("missing_skills", [r["skill"] for r in rows if r.get("current_score", 0) < r.get("required_score", 70)])
    return gap

@app.get("/api/health", tags=["System"])
def health_check():
    return {"status": "ok", "service": "CareerGuide AI API", "version": "1.0.0"}

@app.get("/api/skills", tags=["Assessment"])
def list_skills():
    return {"count": len(SKILL_LABELS), "skills": [{"key": k, "label": v} for k, v in SKILL_LABELS.items()]}


@app.post("/api/assessment/questions", tags=["Assessment"])
def assessment_questions(payload: QuestionsRequest):
    validate_ratings(payload.self_ratings, payload.branch)

    questions = get_adaptive_questions(
        payload.self_ratings,
        questions_per_skill=3,
        branch=payload.branch,
        semester=payload.semester
    )

    
    safe = [
        {
            "question_id": i,
            "skill": q["skill"],
            "difficulty": q.get(
                "difficulty",
                get_difficulty(payload.self_ratings[q["skill"]])
            ),
            "question": q["question"],
            "options": q["options"]
        }
        for i, q in enumerate(questions)
    ]


    return {
        "question_count": len(safe),
        "questions_per_skill": 3,
        "questions": safe
    }


@app.post("/api/assessment/score", tags=["Assessment"])
def score_assessment(payload: ScoreRequest):
    validate_ratings(payload.self_ratings, payload.branch)
    
    questions = get_adaptive_questions(
        payload.self_ratings,
        questions_per_skill=3,
        branch=payload.branch,
        semester=payload.semester
    )

    by_id = dict(enumerate(questions))
    quiz_answers = {skill: [] for skill in payload.self_ratings}
    seen = set()
    for response in payload.responses:
        if response.question_id not in by_id:
            raise HTTPException(status_code=422, detail=f"Invalid question_id: {response.question_id}")
        if response.question_id in seen:
            raise HTTPException(status_code=422, detail=f"Duplicate question_id: {response.question_id}")
        seen.add(response.question_id)
        question = by_id[response.question_id]
        if response.skill != question["skill"]:
            raise HTTPException(status_code=422, detail=f"Skill does not match question_id {response.question_id}.")
        if response.selected_option not in question["options"]:
            raise HTTPException(status_code=422, detail=f"Invalid option for question_id {response.question_id}.")
        quiz_answers[question["skill"]].append((response.selected_option, question))
    if len(seen) != len(questions):
        raise HTTPException(status_code=422, detail=f"Answer all {len(questions)} questions before requesting scores.")
    results = calculate_skill_scores(payload.self_ratings, quiz_answers)
    return {"question_count": len(questions), "weighting": {"self_assessment_percent": 40, "objective_assessment_percent": 60}, "skill_results": results}

@app.post("/api/recommendations", tags=["Career Guidance"])
def career_recommendations(payload: CareerRequest):
    profile = build_profile(payload)
    careers = recommend_careers(profile, top_n=payload.top_n)
    return {"recommendations": [get_career_match_details(profile, career) for career in careers]}

@app.post("/api/skill-gap", tags=["Career Guidance"])
def career_skill_gap(payload: SkillGapRequest):
    profile = build_profile(payload)
    details = get_career_match_details(profile, payload.career)
    gap = enrich_gap(analyze_skill_gap(profile, payload.career), details)
    return {"career": payload.career, "match_details": details, "skill_gap": gap}

@app.post("/api/roadmap", tags=["Career Guidance"])
def career_roadmap(payload: SkillGapRequest):
    profile = build_profile(payload)
    details = get_career_match_details(profile, payload.career)
    gap = enrich_gap(analyze_skill_gap(profile, payload.career), details)
    return generate_roadmap(gap)
