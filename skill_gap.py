CAREER_SKILL_MAP = {
    "Data Analyst": [
        "python",
        "sql",
        "excel",
        "data visualization",
        "statistics"
    ],

    "Web Developer": [
        "html",
        "css",
        "javascript"
    ],

    "Machine Learning Engineer": [
        "python",
        "machine learning",
        "statistics"
    ],

    "Backend Developer": [
        "python",
        "java",
        "databases",
        "sql"
    ],

    "Frontend Developer": [
        "html",
        "css",
        "javascript",
        "react"
    ]
}


def analyze_skill_gap(
    user_profile,
    career,
    required_score=70
):

    skill_scores = user_profile.get(
        "skill_scores",
        {}
    )

    required_skills = CAREER_SKILL_MAP.get(
        career,
        []
    )

    skill_rows = []
    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        current_score = round(
            float(
                skill_scores.get(
                    skill,
                    0
                )
            )
        )

        gap = max(
            0,
            required_score - current_score
        )

        if current_score >= required_score:

            status = "Ready"
            priority = "Complete"

            matched_skills.append(
                skill
            )

        elif gap >= 30:

            status = "Needs improvement"
            priority = "High"

            missing_skills.append(
                skill
            )

        elif gap >= 15:

            status = "Needs improvement"
            priority = "Medium"

            missing_skills.append(
                skill
            )

        else:

            status = "Almost ready"
            priority = "Low"

            missing_skills.append(
                skill
            )

        skill_rows.append(
            {
                "skill": skill,
                "current_score": current_score,
                "required_score": required_score,
                "gap": gap,
                "status": status,
                "priority": priority
            }
        )

    skill_rows.sort(
        key=lambda row: (
            -row["gap"],
            row["skill"]
        )
    )

    if skill_rows:

        coverage = round(
            sum(
                min(
                    row["current_score"],
                    required_score
                )
                for row in skill_rows
            )
            /
            (
                len(skill_rows)
                * required_score
            )
            * 100
        )

    else:

        coverage = 0

    return {
        "career": career,
        "required_score": required_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "skill_rows": skill_rows,
        "coverage": min(
            coverage,
            100
        )
    }