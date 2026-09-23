SKILL_LABELS = {
    "python": "Python",
    "sql": "SQL",
    "excel": "Excel",
    "data visualization": "Data Visualization",
    "statistics": "Statistics",
    "html": "HTML",
    "css": "CSS",
    "javascript": "JavaScript",
    "react": "React",
    "java": "Java",
    "databases": "Databases",
    "machine learning": "Machine Learning",
}


QUESTIONS = [
    {
        "skill": "python",
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "define", "fun"],
        "answer": "def",
    },
    {
        "skill": "sql",
        "question": "Which SQL command is used to retrieve data from a table?",
        "options": ["INSERT", "UPDATE", "SELECT", "DELETE"],
        "answer": "SELECT",
    },
    {
        "skill": "excel",
        "question": "Which Excel function is commonly used to calculate the total of a range?",
        "options": ["SUM", "COUNT", "AVERAGE", "MAX"],
        "answer": "SUM",
    },
    {
        "skill": "data visualization",
        "question": "Which chart is commonly used to compare values across categories?",
        "options": [
            "Bar chart",
            "Pie chart only",
            "Scatter plot only",
            "Box plot only",
        ],
        "answer": "Bar chart",
    },
    {
        "skill": "statistics",
        "question": "Which measure represents the middle value of an ordered dataset?",
        "options": ["Mean", "Median", "Mode", "Range"],
        "answer": "Median",
    },
    {
        "skill": "html",
        "question": "Which HTML tag is used to create a hyperlink?",
        "options": ["<link>", "<a>", "<href>", "<url>"],
        "answer": "<a>",
    },
    {
        "skill": "css",
        "question": "Which CSS property changes the text color?",
        "options": [
            "font-color",
            "text-color",
            "color",
            "foreground",
        ],
        "answer": "color",
    },
    {
        "skill": "javascript",
        "question": "Which operator checks strict equality in JavaScript?",
        "options": ["=", "==", "===", "!="],
        "answer": "===",
    },
    {
        "skill": "react",
        "question": "What is a reusable UI building block in React called?",
        "options": [
            "Component",
            "Selector",
            "Query",
            "Module only",
        ],
        "answer": "Component",
    },
    {
        "skill": "java",
        "question": "Which keyword is used to create an object in Java?",
        "options": [
            "class",
            "new",
            "object",
            "create",
        ],
        "answer": "new",
    },
    {
        "skill": "databases",
        "question": "What is a primary key mainly used for?",
        "options": [
            "Storing duplicate records",
            "Uniquely identifying records",
            "Formatting a table",
            "Deleting a database",
        ],
        "answer": "Uniquely identifying records",
    },
    {
        "skill": "machine learning",
        "question": "Which type of learning uses labelled training data?",
        "options": [
            "Unsupervised Learning",
            "Supervised Learning",
            "Reinforcement Learning",
            "Random Learning",
        ],
        "answer": "Supervised Learning",
    },
]


def calculate_skill_scores(self_ratings, quiz_answers):
    """
    Combine self-confidence and objective quiz performance
    for each skill.

    Self-assessment = 40%
    Objective quiz = 60%
    """

    quiz_lookup = {
        question["skill"]: question
        for question in QUESTIONS
    }

    results = {}

    for skill in SKILL_LABELS:

        self_rating = int(
            self_ratings.get(skill, 3)
        )

        # 1–5 becomes 20–100
        self_score = self_rating * 20

        question = quiz_lookup.get(skill)
        selected_answer = quiz_answers.get(skill)

        objective_score = (
            100
            if question
            and selected_answer == question["answer"]
            else 0
        )

        final_score = round(
            (self_score * 0.40)
            + (objective_score * 0.60)
        )

        results[skill] = {
            "self_score": self_score,
            "objective_score": objective_score,
            "score": final_score,
        }

    return results


def get_skill_level(score):

    if score >= 80:
        return "Advanced"

    if score >= 60:
        return "Intermediate"

    if score >= 40:
        return "Basic"

    return "Beginner"


def get_skill_profile(skill_results):

    return {
        skill: details["score"]
        for skill, details in skill_results.items()
    }