from pytest import fixture


@fixture
def client():
    from demo_pytest import app

    return app.test_client()
