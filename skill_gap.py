from recommendation import CAREER_SKILL_MAP

def analyze_skill_gap(user_profile, career):
    user_skills = set([s.lower() for s in user_profile["skills"]])
    required_skills = set(CAREER_SKILL_MAP.get(career, []))

    missing_skills = required_skills - user_skills
    matched_skills = user_skills.intersection(required_skills)

    return {
        "career": career,
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills)
    }
