def test_response_properties(client):
    payload = {"data": [0, 10, -5, 3]}

    response = client.post("/sort-list", json=payload)

    status_code = response.status_code
    response_type = type(response.json)
    response_payload = response.json
    expected_response_payload = {"data": [-5, 0, 3, 10]}

    assert response.status_code == 200
    assert response_type is dict
    assert response_payload == expected_response_payload


def test_response_properties_fail(client):
    payload = {"data": "string_teste"}

    response = client.post("/sort-list", json=payload)

    status_code = response.status_code
    response_type = type(response.json)
    response_payload = response.json
    expected_response_payload = {
        "error": 'o body deve conter o formato {"data": <lista>}'
    }

    assert response.status_code == 400
    assert response_type is dict
    assert response_payload == expected_response_payload
