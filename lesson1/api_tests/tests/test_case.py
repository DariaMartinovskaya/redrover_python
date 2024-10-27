import functions as func

#Test 1. GET
def test_get_all_test_cases():
    print("\n=== Starting Test: Create New Test Case ===")
    response = func.get_all_test_cases()

    print("\nReceived Response Status Code:")
    print(response.status_code)

    assert response.status_code == 200, "Status code is not 200!"

    print("\nTest passed: the status code is 200!")



#Test 2. POST
def test_create_new_test_case():
    expected_data = {
    "id": 0,
    "name": "TestCasePOST",
    "description": "This test checks if the test case is created",
    "steps": [
      "Step 1: Fill in all fields with valid data. Step 2: Click the Add Test Case button."
    ],
    "expected_result": "Test Case is created and listed",
    "priority": "высокий"
    }

    print("\n=== Starting Test: Create New Test Case ===")
    print("Expected Data:")
    print(expected_data)


    response = func.create_new_test_case()
    response_data = response.json()

    print("\nReceived Response:")
    print(response_data)


# Checking that data is the same as expected data

    assert response_data["name"] == expected_data["name"]

    assert response_data == expected_data, "Test Case data does not match expected values"

    print("\nTest passed: The response matches the expected data!")

#Test 3. PUT

def test_update_test_case():
# Creating new test case (initial data)
    initial_data = {
    "id": 0,
    "name": "TestCasePOST",
    "description": "This test checks if the test case is created",
    "steps": [
      "Step 1: Fill in all fields with valid data. Step 2: Click the Add Test Case button."
    ],
    "expected_result": "Test Case is created and listed",
    "priority": "высокий"
    }

# Creating a new test case by using function
    new_test_case = func.create_new_test_case()
    print("Create Test Case Response:", new_test_case)

# Receiving new test case's ID
    id_ = new_test_case.json().get("testcaseid")
    if id_ is None:
        print("Failed to get test case ID from response. Check response for creation.")
        return
    print("Created Test Case ID:", id_)

    updated_data = {
        "name": "TestCasePUT",
        "description": "This test checks if the test case is updated",
        "steps": [
            "Step 1: Check if all fields are updated correctly."
        ],
        "expected_result": "Test case is updated successfully",
        "priority": "низкий"
    }

    updated_test_case_response = func.put_test_case(id_)
    print("Update Test Case Response:", updated_test_case_response)

    assert updated_test_case_response.status_code == 200, "Update failed!"


    response_data = updated_test_case_response.json()
    print("Updated Test Case Data:", response_data)

    assert response_data["name"] == updated_data["name"], "Name does not match!"
    assert response_data["description"] == updated_data["description"], "Description does not match!"
    assert response_data["priority"] == updated_data["priority"], "Priority does not match!"

    print("\nTest passed: the status code is 200!")

#Test 4. Delete
def test_delete_test_case():
# Creating new test case (initial data)
    initial_data = {
        "id": 0,
        "name": "TestCasePOST",
        "description": "This test checks if the test case is created",
        "steps": [
            "Step 1: Fill in all fields with valid data. Step 2: Click the Add Test Case button."
        ],
        "expected_result": "Test Case is created and listed",
        "priority": "высокий"
    }

    new_test_case = func.create_new_test_case()
    print(new_test_case)

# Receiving new test case's ID
    id_ = new_test_case.json().get("testcaseid")
    if id_ is None:
        print("Failed to get test case ID from response. Check response for creation.")
        return
    print("Created Test Case ID:", id_)

# Deleting test case data using DELETE
    delete_test_case = func.delete_test_case(id_)
    print(delete_test_case.status_code)

# Receiving test case data by ID (it is expected that there is no test case with requested id)
    response = func.get_test_case_by_id(id_)

    print(response.status_code)

# Checking that there is no test case with requested id
    assert response.status_code == 404
