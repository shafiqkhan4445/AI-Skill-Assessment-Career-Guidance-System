
"""Personalized learning roadmap generation with starter resources."""

RESOURCE_MAP = {
    "python": {
        "learn_url": "https://docs.python.org/3/tutorial/",
        "learn_label": "Python Official Tutorial",
        "video_url": "https://www.youtube.com/results?search_query=Python+full+course+beginner+freeCodeCamp",
    },
    "java": {
        "learn_url": "https://dev.java/learn/",
        "learn_label": "Java Learn — dev.java",
        "video_url": "https://www.youtube.com/results?search_query=Java+full+course+beginner+freeCodeCamp",
    },
    "sql": {
        "learn_url": "https://www.postgresql.org/docs/current/tutorial.html",
        "learn_label": "PostgreSQL SQL Tutorial",
        "video_url": "https://www.youtube.com/results?search_query=SQL+full+course+beginner+freeCodeCamp",
    },
    "excel": {
        "learn_url": "https://support.microsoft.com/en-us/excel/",
        "learn_label": "Microsoft Excel Help & Learning",
        "video_url": "https://www.youtube.com/results?search_query=Excel+full+course+data+analysis+beginner",
    },
    "data visualization": {
        "learn_url": "https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-data-visualization/",
        "learn_label": "Microsoft Learn — Data Visualization",
        "video_url": "https://www.youtube.com/results?search_query=data+visualization+full+course+Power+BI+beginner",
    },
    "statistics": {
        "learn_url": "https://www.khanacademy.org/math/statistics-probability",
        "learn_label": "Khan Academy — Statistics & Probability",
        "video_url": "https://www.youtube.com/results?search_query=statistics+and+probability+full+course+beginner",
    },
    "html": {
        "learn_url": "https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content",
        "learn_label": "MDN — HTML",
        "video_url": "https://www.youtube.com/results?search_query=HTML+full+course+beginner+freeCodeCamp",
    },
    "css": {
        "learn_url": "https://developer.mozilla.org/en-US/docs/Web/CSS/Tutorials",
        "learn_label": "MDN — CSS Tutorials",
        "video_url": "https://www.youtube.com/results?search_query=CSS+full+course+beginner+freeCodeCamp",
    },
    "javascript": {
        "learn_url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
        "learn_label": "MDN — JavaScript Guide",
        "video_url": "https://www.youtube.com/results?search_query=JavaScript+full+course+beginner+freeCodeCamp",
    },
    "react": {
        "learn_url": "https://react.dev/learn",
        "learn_label": "React Official Learn",
        "video_url": "https://www.youtube.com/results?search_query=React+full+course+beginner+freeCodeCamp",
    },
    "machine learning": {
        "learn_url": "https://scikit-learn.org/stable/getting_started.html",
        "learn_label": "scikit-learn — Getting Started",
        "video_url": "https://www.youtube.com/results?search_query=machine+learning+full+course+beginner+freeCodeCamp",
    },
    "databases": {
        "learn_url": "https://dev.mysql.com/doc/mysql-tutorial-excerpt/8.4/en/",
        "learn_label": "MySQL Tutorial",
        "video_url": "https://www.youtube.com/results?search_query=database+management+systems+DBMS+full+course+beginner",
    },

    # ECE resources
    "c programming": {
        "learn_url": "https://www.learn-c.org/",
        "learn_label": "Learn-C.org Interactive Tutorial",
        "video_url": "https://www.youtube.com/results?search_query=embedded+C+programming+beginner",
    },
    "circuit analysis": {
        "learn_url": "https://www.allaboutcircuits.com/textbook/",
        "learn_label": "All About Circuits Textbook",
        "video_url": "https://www.youtube.com/results?search_query=basic+circuit+analysis+course",
    },
    "digital electronics": {
        "learn_url": "https://www.allaboutcircuits.com/textbook/digital/",
        "learn_label": "All About Circuits — Digital",
        "video_url": "https://www.youtube.com/results?search_query=digital+electronics+course",
    },
    "analog electronics": {
        "learn_url": "https://www.allaboutcircuits.com/textbook/semiconductors/",
        "learn_label": "All About Circuits — Semiconductors",
        "video_url": "https://www.youtube.com/results?search_query=analog+electronics+course",
    },
    "signals and systems": {
        "learn_url": "https://ocw.mit.edu/",
        "learn_label": "MIT OpenCourseWare",
        "video_url": "https://www.youtube.com/results?search_query=signals+and+systems+course",
    },
    "communication systems": {
        "learn_url": "https://ocw.mit.edu/",
        "learn_label": "MIT OpenCourseWare",
        "video_url": "https://www.youtube.com/results?search_query=digital+communications+course",
    },
    "microcontrollers": {
        "learn_url": "https://docs.arduino.cc/",
        "learn_label": "Arduino Documentation",
        "video_url": "https://www.youtube.com/results?search_query=microcontrollers+beginner+tutorial",
    },
    "embedded systems": {
        "learn_url": "https://docs.arduino.cc/",
        "learn_label": "Arduino Documentation",
        "video_url": "https://www.youtube.com/results?search_query=embedded+systems+beginner+course",
    },
    "vlsi basics": {
        "learn_url": "https://www.electronics-tutorials.ws/",
        "learn_label": "Electronics Tutorials",
        "video_url": "https://www.youtube.com/results?search_query=VLSI+design+basics+course",
    },
    "matlab": {
        "learn_url": "https://www.mathworks.com/help/matlab/",
        "learn_label": "MATLAB Documentation",
        "video_url": "https://www.youtube.com/results?search_query=MATLAB+basics+course",
    },
    "pcb design": {
        "learn_url": "https://docs.kicad.org/",
        "learn_label": "KiCad Documentation",
        "video_url": "https://www.youtube.com/results?search_query=PCB+design+KiCad+beginner",
    },
}


ROADMAP_TEMPLATES = {
    "python": {
        "learn": "Revise Python syntax, functions, collections and Pandas.",
        "practice": "Solve 10–15 small Python problems using lists, dictionaries and functions.",
        "build": "Build a small data-processing or automation project in Python.",
    },
    "java": {
        "learn": "Revise Java OOP, collections, exception handling and core syntax.",
        "practice": "Solve object-oriented programming and collection-based coding exercises.",
        "build": "Build a small Java application such as a library or student-management system.",
    },
    "sql": {
        "learn": "Learn SELECT, filtering, joins, grouping, subqueries and aggregate functions.",
        "practice": "Write SQL queries on a sample database and solve progressively harder query problems.",
        "build": "Create a small relational database and write queries for a real use case.",
    },
    "excel": {
        "learn": "Learn formulas, functions, sorting, filtering, lookups and PivotTables.",
        "practice": "Clean a small dataset and answer analysis questions using Excel functions.",
        "build": "Build an Excel dashboard that summarizes a realistic business dataset.",
    },
    "data visualization": {
        "learn": "Learn chart selection, dashboards, visual storytelling and interactive visualization.",
        "practice": "Create several chart types from one dataset and explain the patterns you see.",
        "build": "Build an interactive dashboard using Plotly, Power BI or another visualization tool.",
    },
    "statistics": {
        "learn": "Learn mean, median, variance, standard deviation, probability and distributions.",
        "practice": "Perform exploratory analysis and interpret basic statistical results.",
        "build": "Create a short statistical analysis report from a real dataset.",
    },
    "html": {
        "learn": "Learn document structure, semantic elements, links, forms and accessibility basics.",
        "practice": "Recreate a few simple pages using semantic HTML and forms.",
        "build": "Build a multi-section personal or portfolio webpage using HTML.",
    },
    "css": {
        "learn": "Learn selectors, the box model, layout, Flexbox, Grid, responsive design and basic animation.",
        "practice": "Style a simple webpage and reproduce several layouts using Flexbox and Grid.",
        "build": "Create a responsive landing page with reusable components and polished styling.",
    },
    "javascript": {
        "learn": "Learn variables, functions, arrays, objects, DOM manipulation and asynchronous JavaScript.",
        "practice": "Solve small JavaScript problems and add interactions to a simple webpage.",
        "build": "Build an interactive browser application such as a quiz, tracker or task manager.",
    },
    "react": {
        "learn": "Learn components, props, state, events, lists, conditional rendering and hooks.",
        "practice": "Build small components and manage state in a simple React application.",
        "build": "Create a complete React project with reusable components and a responsive interface.",
    },
    "machine learning": {
        "learn": "Learn supervised vs unsupervised learning, preprocessing, features, training and evaluation.",
        "practice": "Train simple classification or regression models and compare their evaluation metrics.",
        "build": "Build a small end-to-end machine-learning project using a public dataset.",
    },
    "databases": {
        "learn": "Learn relational databases, keys, normalization, relationships and transactions.",
        "practice": "Design a small schema and write queries for common database operations.",
        "build": "Build a database-backed application with a clear relational schema.",
    },

    # ECE roadmap steps
    "c programming": {
        "learn": "Study C syntax, functions, pointers, arrays and memory basics for embedded programming.",
        "practice": "Write small C programs using arrays, pointers and bitwise operations.",
        "build": "Build a simple sensor-reading or microcontroller program.",
    },
    "circuit analysis": {
        "learn": "Review Ohm's law, Kirchhoff's laws, network theorems and AC circuit fundamentals.",
        "practice": "Solve circuit problems involving voltage, current, resistance and equivalent networks.",
        "build": "Simulate and document a basic DC or AC circuit.",
    },
    "digital electronics": {
        "learn": "Study logic gates, Boolean algebra, combinational circuits and sequential circuits.",
        "practice": "Simplify Boolean expressions and solve logic-circuit exercises.",
        "build": "Design a simple counter or digital logic circuit.",
    },
    "analog electronics": {
        "learn": "Review diodes, transistors, amplifiers and semiconductor fundamentals.",
        "practice": "Analyze basic diode and transistor circuits.",
        "build": "Simulate a simple amplifier circuit.",
    },
    "signals and systems": {
        "learn": "Study continuous and discrete signals, system properties, convolution and transforms.",
        "practice": "Solve signal classification and basic convolution problems.",
        "build": "Plot and analyze sample signals using MATLAB or Python.",
    },
    "communication systems": {
        "learn": "Study modulation, demodulation, bandwidth, noise and digital communication fundamentals.",
        "practice": "Compare modulation techniques and solve basic communication problems.",
        "build": "Simulate a basic modulation and demodulation example.",
    },
    "microcontrollers": {
        "learn": "Learn microcontroller architecture, GPIO, timers and sensor interfacing.",
        "practice": "Write programs to read inputs and control outputs on a development board.",
        "build": "Create a simple sensor or LED-control prototype.",
    },
    "embedded systems": {
        "learn": "Study embedded C, hardware-software interaction and basic real-time concepts.",
        "practice": "Practice GPIO control, sensor reading and debugging.",
        "build": "Build a small embedded prototype using a microcontroller.",
    },
    "vlsi basics": {
        "learn": "Study digital logic design, CMOS fundamentals and the VLSI design flow.",
        "practice": "Practice Boolean simplification and basic digital circuit design.",
        "build": "Create a small digital design and document its logic.",
    },
    "matlab": {
        "learn": "Learn MATLAB variables, vectors, matrices, plots and basic scripts.",
        "practice": "Write scripts to calculate values and plot signals.",
        "build": "Create a simulation or visualization of an engineering concept.",
    },
    "pcb design": {
        "learn": "Learn schematic capture, footprints, routing, design rules and PCB layout basics.",
        "practice": "Create a schematic and route a simple two-layer board.",
        "build": "Design a small PCB and run design-rule checks.",
    },
}


def generate_roadmap(skill_gap_result):
    """Generate learning steps for the selected career's missing skills."""
    missing_skills = skill_gap_result.get("missing_skills", [])
    skill_rows = {
        row["skill"]: row
        for row in skill_gap_result.get("skill_rows", [])
    }

    roadmap = []

    for skill in missing_skills:
        skill_key = skill.lower()
        row = skill_rows.get(skill)

        template = ROADMAP_TEMPLATES.get(
            skill_key,
            {
                "learn": f"Learn the core concepts of {skill.title()}.",
                "practice": f"Complete guided exercises using {skill.title()}.",
                "build": f"Build a small practical project using {skill.title()}.",
            },
        )

        resources = RESOURCE_MAP.get(skill_key, {})

        step = {
            "skill": skill,
            "learn": template["learn"],
            "practice": template["practice"],
            "build": template["build"],
            "learn_url": resources.get(
                "learn_url",
                "https://www.google.com/search?q="
                + skill.replace(" ", "+")
                + "+tutorial",
            ),
            "learn_label": resources.get(
                "learn_label",
                f"{skill.title()} Learning Resource",
            ),
            "video_url": resources.get(
                "video_url",
                "https://www.youtube.com/results?search_query="
                + skill.replace(" ", "+")
                + "+tutorial",
            ),
        }

        if row:
            step.update(
                {
                    "current_score": row.get("current_score", 0),
                    "required_score": row.get("required_score", 70),
                    "gap": row.get("gap", 0),
                    "priority": row.get("priority", "Low"),
                }
            )
        else:
            step.update(
                {
                    "current_score": 0,
                    "required_score": 70,
                    "gap": 70,
                    "priority": "Low",
                }
            )

        roadmap.append(step)

    roadmap.sort(
        key=lambda item: (
            -item["gap"],
            -{
                "High": 3,
                "Medium": 2,
                "Low": 1,
                "Complete": 0,
            }.get(item["priority"], 0),
        )
    )

    return {
        "career": skill_gap_result.get("career", ""),
        "roadmap_steps": roadmap,
    }
