from demo_pytest import app


# def test_return_status_code():
#     client = app.test_client()
#     response = client.get("/dict")

#     assert response.status_code == 200


# def test_return_type():
#     client = app.test_client()
#     response = client.get("/dict")

#     assert type(response.json) is dict


# def test_return_body():
#     client = app.test_client()
#     response = client.get("/dict")
#     expected = {"key": "value"}

#     assert (
#         response.json == expected
#     ), "Vefique se o retorno da rota `/dict` está como o esperado"


def test_return_properties():
    client = app.test_client()
    response = client.get("/dict")

    status_code = response.status_code
    response_type = type(response.json)
    response_payload = response.json
    expected_response_payload = {"key": "value"}

    assert response.status_code == 200
    assert response_type is dict
    assert response_payload == expected_response_payload
