CAREER_PROFILES = {

    "Data Analyst": {
        "skills": [
            "python",
            "sql",
            "excel",
            "data visualization",
            "statistics"
        ],
        "description":
            "Turn data into useful insights, reports and decisions."
    },

    "Web Developer": {
        "skills": [
            "html",
            "css",
            "javascript"
        ],
        "description":
            "Build and maintain modern websites and web applications."
    },

    "Machine Learning Engineer": {
        "skills": [
            "python",
            "machine learning",
            "statistics"
        ],
        "description":
            "Build and evaluate machine-learning solutions from data."
    },

    "Backend Developer": {
        "skills": [
            "python",
            "java",
            "databases",
            "sql"
        ],
        "description":
            "Develop APIs, server-side logic and database-driven systems."
    },

    "Frontend Developer": {
        "skills": [
            "html",
            "css",
            "javascript",
            "react"
        ],
        "description":
            "Create interactive and responsive user interfaces."
    }
}


# Compatibility with the rest of the project
CAREER_SKILL_MAP = {
    career: data["skills"]
    for career, data in CAREER_PROFILES.items()
}


def get_career_match_details(
    user_profile,
    career,
    target_score=70
):

    required_skills = CAREER_SKILL_MAP.get(
        career,
        []
    )

    skill_scores = user_profile.get(
        "skill_scores",
        {}
    )

    skill_rows = []

    for skill in required_skills:

        current_score = round(
            float(
                skill_scores.get(
                    skill,
                    0
                )
            )
        )

        skill_rows.append(
            {
                "skill": skill,
                "current_score": current_score,
                "required_score": target_score,
                "gap": max(
                    0,
                    target_score - current_score
                )
            }
        )


    if skill_rows:

        match_score = round(
            sum(
                row["current_score"]
                for row in skill_rows
            )
            /
            len(skill_rows)
        )

    else:

        match_score = 0


    matched_skills = [
        row["skill"]
        for row in skill_rows
        if row["current_score"]
        >= target_score
    ]


    return {
        "career": career,
        "description":
            CAREER_PROFILES[
                career
            ]["description"],

        "match_score":
            min(match_score, 100),

        "required_skills":
            required_skills,

        "matched_skills":
            matched_skills,

        "skill_rows":
            skill_rows
    }


def recommend_careers(
    user_profile,
    top_n=3
):

    scored_careers = []

    for career in CAREER_PROFILES:

        details = (
            get_career_match_details(
                user_profile,
                career
            )
        )

        scored_careers.append(
            (
                career,
                details["match_score"]
            )
        )


    scored_careers.sort(
        key=lambda item: (
            -item[1],
            item[0]
        )
    )


    return [
        career
        for career, score
        in scored_careers[
            :top_n
        ]
    ]