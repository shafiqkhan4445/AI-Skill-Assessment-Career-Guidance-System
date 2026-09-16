def generate_roadmap(skill_gap_result):
    missing_skills = skill_gap_result["missing_skills"]

    roadmap = []

    for skill in missing_skills:
        roadmap.append({
            "skill": skill,
            "resources": f"Learn {skill} via online courses (YouTube, Coursera, Udemy)",
            "project": f"Build a project using {skill}"
        })

    return {
        "career": skill_gap_result["career"],
        "roadmap_steps": roadmap
    }
