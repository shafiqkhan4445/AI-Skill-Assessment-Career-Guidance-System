ROADMAP_TEMPLATES = {

    "python": {
        "learn":
            "Revise Python syntax, functions, collections and Pandas.",

        "practice":
            "Solve 10–15 small Python problems using lists, dictionaries and functions.",

        "build":
            "Build a small data-processing or automation project in Python."
    },

    "sql": {
        "learn":
            "Learn SELECT, WHERE, JOIN, GROUP BY, aggregate functions and subqueries.",

        "practice":
            "Practice SQL queries using a small relational dataset.",

        "build":
            "Build a student or sales database and create an analysis report."
    },

    "excel": {
        "learn":
            "Learn formulas, IF, lookup functions, sorting, filtering and PivotTables.",

        "practice":
            "Clean a small dataset and create summary tables.",

        "build":
            "Create an Excel dashboard from a real-world dataset."
    },

    "data visualization": {
        "learn":
            "Learn chart selection, dashboards, visual storytelling and interactive visualisation.",

        "practice":
            "Create charts from one dataset and explain the patterns you see.",

        "build":
            "Build an interactive dashboard using Plotly or another visualization tool."
    },

    "statistics": {
        "learn":
            "Learn mean, median, variance, standard deviation, probability and distributions.",

        "practice":
            "Perform exploratory analysis and interpret basic statistical results.",

        "build":
            "Create a short statistical analysis report from a real dataset."
    },

    "html": {
        "learn":
            "Learn semantic HTML, forms, tables, links and page structure.",

        "practice":
            "Recreate a simple webpage using HTML.",

        "build":
            "Build a personal portfolio or student profile page."
    },

    "css": {
        "learn":
            "Learn selectors, box model, Flexbox, Grid and responsive design.",

        "practice":
            "Style an existing HTML page for desktop and mobile.",

        "build":
            "Build a responsive landing page."
    },

    "javascript": {
        "learn":
            "Learn variables, functions, arrays, objects, DOM manipulation and events.",

        "practice":
            "Build small interactive JavaScript exercises.",

        "build":
            "Create an interactive quiz or task-tracker application."
    },

    "react": {
        "learn":
            "Learn components, props, state, events and basic React hooks.",

        "practice":
            "Convert a small page into reusable React components.",

        "build":
            "Build a small React dashboard or task-management application."
    },

    "java": {
        "learn":
            "Revise classes, objects, inheritance, collections and exception handling.",

        "practice":
            "Solve Java programming problems using OOP concepts.",

        "build":
            "Build a small Java application using classes and collections."
    },

    "databases": {
        "learn":
            "Learn tables, relationships, primary keys, foreign keys and normalization.",

        "practice":
            "Design a small relational schema and write basic queries.",

        "build":
            "Build a small database-backed application."
    },

    "machine learning": {
        "learn":
            "Learn supervised learning, classification, train/test split and evaluation metrics.",

        "practice":
            "Train a simple classification model on a small dataset.",

        "build":
            "Build a small ML project and explain its features and evaluation."
    }
}


def generate_roadmap(
    skill_gap_result
):

    roadmap_steps = []


    for row in skill_gap_result.get(
        "skill_rows",
        []
    ):

        if row["gap"] <= 0:
            continue


        template = ROADMAP_TEMPLATES.get(

            row["skill"],

            {
                "learn":
                    f"Study the core concepts of {row['skill'].title()}.",

                "practice":
                    f"Complete practical exercises using {row['skill'].title()}.",

                "build":
                    f"Build a small project demonstrating {row['skill'].title()}."
            }
        )


        roadmap_steps.append(
            {
                **row,

                "learn":
                    template["learn"],

                "practice":
                    template["practice"],

                "build":
                    template["build"]
            }
        )


    return {

        "career":
            skill_gap_result.get(
                "career",
                ""
            ),

        "roadmap_steps":
            roadmap_steps
    }