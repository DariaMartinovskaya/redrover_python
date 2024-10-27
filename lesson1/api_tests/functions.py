import requests

from pprint import pprint

URL = "http://127.0.0.1:8000/testcases/"
URL_CREATE = "http://127.0.0.1:8000/testcases/"

def get_test_case_by_id(id_):
    response = requests.get(URL + f"{id_}")

    return response

# response = get_test_case_by_id(30)
# pprint(response.status_code)
# if response.status_code == 200:
#     pprint(response.json())

print("")
def get_all_test_cases():
    return requests.get(URL)

response = get_all_test_cases()

if response.status_code == 200:
    pprint(response.json())

print("")
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

# response = create_new_test_case()
# pprint(response.status_code)
# print('')
# pprint(response.json())
#
# print("________")
def put_test_case(id_):
    info = {
        "name": "TestCasePUT",
        "description": "This test checks if the test case is updated",
        "steps": [
            "Step 1: Check if all fields are updated correctly."
        ],
        "expected_result": "Test case is updated successfully",
        "priority": "низкий"
    }

    response = requests.put(URL + f"{id_}", json=info)

    return response

# test_case_id = 0
# response = put_test_case(test_case_id)
#
# print("Response Status Code:", response.status_code)
# print("Response Content:")
# pprint(response.json())

print("________")
def delete_test_case(id_):

    response = requests.delete(URL + f"{id_}")

    return response

# test_case_id = 0
# response = delete_test_case(test_case_id)
#
# print("Response Status Code:", response.status_code)
# print("Response Content:")
# pprint(response.json())