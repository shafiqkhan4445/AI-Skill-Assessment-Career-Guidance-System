
import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

BASE_URL = "http://127.0.0.1:8000"

ratings = {
    "python": 3,
    "sql": 3,
    "excel": 3,
    "data visualization": 3,
    "statistics": 3,
    "html": 3,
    "css": 3,
    "javascript": 3,
    "react": 3,
    "java": 3,
    "databases": 3,
    "machine learning": 3
}

def post_json(path, payload):
    data = json.dumps(payload).encode("utf-8")
    request = Request(
        BASE_URL + path,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    with urlopen(request, timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))

try:
    print("1. Requesting assessment questions...")
    question_result = post_json(
        "/api/assessment/questions",
        {"self_ratings": ratings}
    )

    questions = question_result["questions"]
    print("Questions received:", len(questions))

    # Select a valid option for every question.
    # These are test answers, not necessarily correct answers.
    responses = [
        {
            "skill": question["skill"],
            "question_id": question["question_id"],
            "selected_option": question["options"][0]
        }
        for question in questions
    ]

    print("2. Submitting answers for scoring...")
    result = post_json(
        "/api/assessment/score",
        {
            "self_ratings": ratings,
            "responses": responses
        }
    )

    print("\nSUCCESS: Assessment scoring endpoint works!")
    print("Questions scored:", result["question_count"])
    print("Weighting:", result["weighting"])
    print("Skill results returned:", len(result["skill_results"]))
    print("\nFull response:")
    print(json.dumps(result, indent=2))

except HTTPError as error:
    print("API returned HTTP error:", error.code)
    print(error.read().decode("utf-8"))

except URLError as error:
    print("Could not connect to the API:", error.reason)

except Exception as error:
    print("Test failed:", error)
