CAREER_SKILL_MAP = {
    "Data Analyst": ["python", "sql", "excel", "data visualization"],
    "Web Developer": ["html", "css", "javascript"],
    "Machine Learning Engineer": ["python", "machine learning", "statistics"],
    "Backend Developer": ["python", "java", "databases"],
    "Frontend Developer": ["html", "css", "javascript", "react"]
}

def recommend_careers(user_profile):
    user_skills = set([s.lower() for s in user_profile["skills"]])
    scores = {}

    for career, skills in CAREER_SKILL_MAP.items():
        match = user_skills.intersection(set(skills))
        scores[career] = len(match)

    
    sorted_careers = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    
    return [career for career, score in sorted_careers if score > 0][:3]
