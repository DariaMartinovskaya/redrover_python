import requests

from pprint import pprint

URL_CREATE = "http://127.0.0.1:8000/testcases/"

def create_new_test_case():
    info = {
    "id": 0,
    "name": "TestCasePOST",
    "description": "This test checks if the test case is created",
    "steps": [
      "Step 1: Fill in all fields with valid data. Step 2: Click the Add Test Case button."
    ],
    "expected_result": "Test Case is created and listed",
    "priority": "высокий"
    }

    response = requests.post(URL_CREATE, json=info)

    return response

response = create_new_test_case()
pprint(response.status_code)
pprint()
pprint(response.json())