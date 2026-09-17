# assessment.py

QUESTIONS = [
    # -------------------- PYTHON --------------------
    {
        "skill": "python",
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "define", "fun"],
        "answer": 2
    },
    {
        "skill": "python",
        "question": "Which data type is used to store True or False?",
        "options": ["int", "string", "boolean", "float"],
        "answer": 3
    },
    {
        "skill": "python",
        "question": "What is the output of: print(2 + 3 * 2)?",
        "options": ["10", "8", "12", "7"],
        "answer": 2
    },

    # -------------------- JAVA --------------------
    {
        "skill": "java",
        "question": "Which keyword is used to create an object in Java?",
        "options": ["class", "new", "object", "create"],
        "answer": 2
    },
    {
        "skill": "java",
        "question": "Which method is the entry point of a Java program?",
        "options": ["start()", "run()", "main()", "execute()"],
        "answer": 3
    },
    {
        "skill": "java",
        "question": "Which concept allows a class to inherit properties from another class?",
        "options": ["Encapsulation", "Inheritance", "Polymorphism", "Abstraction"],
        "answer": 2
    },

    # -------------------- SQL --------------------
    {
        "skill": "sql",
        "question": "Which SQL command is used to retrieve data?",
        "options": ["INSERT", "UPDATE", "SELECT", "DELETE"],
        "answer": 3
    },
    {
        "skill": "sql",
        "question": "Which SQL clause is used to filter records?",
        "options": ["ORDER BY", "WHERE", "GROUP BY", "FROM"],
        "answer": 2
    },
    {
        "skill": "sql",
        "question": "Which command is used to add a new record to a table?",
        "options": ["ADD", "INSERT", "CREATE", "UPDATE"],
        "answer": 2
    },

    # -------------------- HTML --------------------
    {
        "skill": "html",
        "question": "Which HTML tag is used to create a hyperlink?",
        "options": ["<link>", "<a>", "<href>", "<url>"],
        "answer": 2
    },
    {
        "skill": "html",
        "question": "Which tag is used for the largest heading?",
        "options": ["<h6>", "<heading>", "<h1>", "<head>"],
        "answer": 3
    },

    # -------------------- CSS --------------------
    {
        "skill": "css",
        "question": "Which property is used to change text color in CSS?",
        "options": ["font-color", "text-color", "color", "foreground"],
        "answer": 3
    },
    {
        "skill": "css",
        "question": "Which symbol is used to select an element by its ID?",
        "options": [".", "#", "*", "&"],
        "answer": 2
    },

    # -------------------- JAVASCRIPT --------------------
    {
        "skill": "javascript",
        "question": "Which keyword can be used to declare a variable in JavaScript?",
        "options": ["var", "int", "string", "define"],
        "answer": 1
    },
    {
        "skill": "javascript",
        "question": "Which symbol is commonly used for strict equality in JavaScript?",
        "options": ["=", "==", "===", "!="],
        "answer": 3
    },

    # -------------------- MACHINE LEARNING --------------------
    {
        "skill": "machine learning",
        "question": "Which type of learning uses labelled training data?",
        "options": [
            "Unsupervised Learning",
            "Supervised Learning",
            "Reinforcement Learning",
            "Random Learning"
        ],
        "answer": 2
    },
    {
        "skill": "machine learning",
        "question": "Which algorithm is commonly used for classification?",
        "options": [
            "Linear Regression",
            "Logistic Regression",
            "K-Means only",
            "PCA"
        ],
        "answer": 2
    },

    # -------------------- STATISTICS --------------------
    {
        "skill": "statistics",
        "question": "What is the mean of 2, 4, and 6?",
        "options": ["3", "4", "5", "6"],
        "answer": 2
    },
    {
        "skill": "statistics",
        "question": "Which measure represents the middle value of an ordered dataset?",
        "options": ["Mean", "Mode", "Median", "Range"],
        "answer": 3
    },

    # -------------------- DATABASES --------------------
    {
        "skill": "databases",
        "question": "What is a primary key used for?",
        "options": [
            "To store duplicate records",
            "To uniquely identify records",
            "To delete a database",
            "To format a table"
        ],
        "answer": 2
    }
]


def conduct_assessment():
    """
    Conduct the student assessment and return the user profile.
    """

    print("\n===================================")
    print("       SKILL ASSESSMENT")
    print("===================================\n")

    name = input("Enter your name: ").strip()

    scores = {}
    total_questions = {}

    for index, question in enumerate(QUESTIONS, start=1):

        skill = question["skill"]

        scores.setdefault(skill, 0)
        total_questions.setdefault(skill, 0)

        total_questions[skill] += 1

        print(f"\nQ{index}. {question['question']}")

        for option_number, option in enumerate(
            question["options"], start=1
        ):
            print(f"{option_number}. {option}")

        while True:
            try:
                answer = int(input("Enter your answer (1-4): "))

                if 1 <= answer <= 4:
                    break

                print("Please enter a number between 1 and 4.")

            except ValueError:
                print("Please enter a valid number.")

        if answer == question["answer"]:
            scores[skill] += 1

    # Calculate skill percentages
    skill_scores = {}

    for skill in total_questions:
        score = (
            scores[skill] / total_questions[skill]
        ) * 100

        skill_scores[skill] = round(score, 2)

    # Skills demonstrated by the student
    # 50% or above = skill included in profile
    user_skills = [
        skill
        for skill, score in skill_scores.items()
        if score >= 50
    ]

    user_profile = {
        "name": name,
        "skills": user_skills,
        "skill_scores": skill_scores
    }

    return user_profile


def display_results(user_profile):
    """
    Display the assessment results.
    """

    print("\n===================================")
    print("       ASSESSMENT RESULTS")
    print("===================================")

    print(f"\nStudent: {user_profile['name']}")

    print("\nSkill Scores:")

    for skill, score in user_profile["skill_scores"].items():

        if score >= 80:
            level = "Advanced"
        elif score >= 60:
            level = "Intermediate"
        elif score >= 50:
            level = "Basic"
        else:
            level = "Beginner"

        print(f"- {skill.title()}: {score}% ({level})")

    print("\nDemonstrated Skills:")

    if user_profile["skills"]:
        for skill in user_profile["skills"]:
            print(f"- {skill.title()}")
    else:
        print("- No skills reached the required threshold.")


if __name__ == "__main__":

    profile = conduct_assessment()

    display_results(profile)