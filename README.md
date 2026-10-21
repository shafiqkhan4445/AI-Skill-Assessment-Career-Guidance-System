# AI-Based Personalized Career Guidance System with Skill Gap Analysis for Students

An AI-based career guidance application that assesses student skills, recommends suitable career paths, identifies skill gaps, and generates personalized learning roadmaps for **CSE, ISE, and ECE students**.

## Project Overview

Choosing a suitable career can be challenging for undergraduate and graduate students who may not know how their current skills align with different career paths. This application helps students understand their technical skill levels and explore career options based on their assessment results.

The application combines self-assessment with adaptive objective assessment to calculate individual skill scores. These scores are used to recommend relevant career paths, compare current skills against target requirements, prioritize skill gaps, and provide a personalized learning roadmap with learning materials.

The system uses an explainable, rule-based career-matching approach rather than a trained machine-learning model.

## Key Features

- **Student Profile:** Collects the student's name, academic branch, and semester.
- **Branch-Specific Assessment:** Supports CSE, ISE, and ECE with relevant technical skills and objective questions.
- **Self-Assessment:** Allows students to rate their confidence in each skill on a scale of 1–5.
- **Adaptive Objective Assessment:** Selects question difficulty based on the student's confidence rating and academic semester.
- **Question Bank:** Provides three objective questions per skill at the selected difficulty level.
- **Skill Score Calculation:** Combines self-assessment and objective assessment scores using a 40% and 60% weighting, respectively.
- **Career Recommendations:** Suggests career paths based on assessed skills and predefined career requirements.
- **Career Match Analysis:** Displays match scores and the skills associated with each recommended career.
- **Skill Gap Analysis:** Compares current skill levels with target requirements and identifies areas for improvement.
- **Skill Gap Prioritization:** Highlights skills that need further development.
- **Personalized Learning Roadmap:** Generates a Learn–Practice–Build plan for identified skill gaps.
- **Learning Resources:** Provides relevant learning references and YouTube learning links for supported skills.
- **Interactive Visualizations:** Presents skill scores, career matches, and skill-gap information through charts and dashboard metrics.
- **REST API:** Uses FastAPI endpoints for assessment questions, skill scoring, and career recommendations.

## Branch Support

| Branch | Assessment Focus | Example Career Paths |
|---|---|---|
| CSE | Programming, databases, web development, statistics, and machine learning | Data Analyst, Web Developer, Backend Developer, Frontend Developer, Machine Learning Engineer |
| ISE | Computing, programming, databases, web development, and data-related skills | Data Analyst, Web Developer, Backend Developer, Frontend Developer, Machine Learning Engineer |
| ECE | Circuit analysis, digital and analog electronics, signals, communication systems, microcontrollers, embedded systems, VLSI basics, MATLAB, and PCB design | Embedded Systems Engineer, Electronics Design Engineer, Communication Systems Engineer |

## System Workflow

1. Student profile creation
2. Branch- and semester-specific skill selection
3. Self-assessment of technical skills
4. Adaptive objective assessment
5. Skill score calculation
6. Career recommendation and match analysis
7. Skill-gap analysis and prioritization
8. Personalized learning roadmap generation
9. Access to learning resources

## Technologies Used

- **Python** — Core application logic and assessment processing
- **Streamlit** — Interactive user interface and results dashboard
- **FastAPI** — REST API for assessment and career recommendation functionality
- **Pandas** — Data handling and processing
- **Scikit-learn** — Available in the project environment for potential future machine-learning extensions; the current career matching is rule-based
- **Plotly** — Interactive charts and skill visualizations

## Project Structure

```text
AI-Career-Guidance-System/
├── app.py
├── api.py
├── assessment.py
├── recommendation.py
├── skill_gap.py
├── roadmap.py
├── test_api.py
├── requirements.txt
├── README.md
└── data/
```

## Installation and Setup

### Prerequisites

- Python 3.11 or a compatible Python version
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/shafiqkhan4445/AI-Skill-Assessment-Career-Guidance-System.git
cd AI-Skill-Assessment-Career-Guidance-System
```

### 2. Create and activate a virtual environment

On Windows:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the FastAPI backend

Open a terminal in the project directory and run:

```bash
uvicorn api:app --reload
```

The API runs at:

`http://127.0.0.1:8000`

Interactive API documentation is available at:

`http://127.0.0.1:8000/docs`

### 5. Start the Streamlit application

Open a second terminal in the project directory, activate the virtual environment if necessary, and run:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

`http://localhost:8501`

Keep the FastAPI backend running while using the Streamlit application because the frontend sends requests to the API.

## API Endpoints

The FastAPI backend provides the following main endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Check API availability |
| GET | `/api/health` | Check API service status |
| GET | `/api/skills` | Retrieve the default skill list |
| POST | `/api/assessment/questions` | Retrieve adaptive assessment questions |
| POST | `/api/assessment/score` | Calculate skill assessment scores |
| POST | `/api/recommendations` | Generate career recommendations |
| POST | `/api/skill-gap` | Analyze skill gaps for a selected career |
| POST | `/api/roadmap` | Generate a learning roadmap for a selected career |

Interactive request and response schemas can be explored through the FastAPI documentation at `/docs`.

## Assessment and Recommendation Logic

The application uses two assessment components:

- **Self-assessment:** Represents the student's reported confidence in a particular skill.
- **Objective assessment:** Evaluates responses to multiple-choice questions selected according to the student's confidence rating and semester.

The current scoring approach combines the components as follows:

**Final Skill Score = (0.40 × Self-Assessment Score) + (0.60 × Objective Assessment Score)**

Career recommendations are generated by comparing the student's skill scores with predefined skill requirements for available careers. Skill-gap analysis then identifies the difference between the student's current scores and the target level. These gaps guide the personalized learning roadmap.

The application is intended to provide initial career guidance and skill-development direction. Its recommendations should not be interpreted as a formal certification of technical competence.

## Team Members

- **Shafiq Ur Rahman Khan** — 20231CSE0249
- **Mohammed Meran Ahmed** — 20231CSE0232
- **Sameer Khan** — 20231CSE0250

## Current Project Status

The core prototype workflow has been implemented and tested, including branch-specific assessment content, skill scoring, career recommendations, skill-gap analysis, and personalized learning roadmaps.

The Streamlit frontend communicates with the FastAPI backend for assessment and recommendation operations. CSE, ISE, and ECE have branch-specific skill and career configurations, with relevant learning resources provided through the roadmap.

The current implementation uses predefined rules and career-skill requirements. A trained machine-learning model and large-scale student evaluation are not part of the current prototype.

## Future Scope

- Add more questions to improve assessment coverage across skills and difficulty levels.
- Refine career recommendations using feedback from students and project evaluators.
- Expand the learning resource collection for CSE, ISE, and ECE.
- Improve the assessment interface and provide clearer explanations of skill scores and gaps.
- Test the application with more students to evaluate its usability and the relevance of its recommendations.
- Explore machine-learning-based career recommendations if suitable datasets become available.

## University

**Presidency University**  
School of Computer Science and Engineering  
Bengaluru, Karnataka, India

**Semester VII — Mini Project (CSE7102)**

