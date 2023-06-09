import pytest as pytest

from project import create_app


import pytest

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

# ============= tests ===================


def test_edit_user(client):
    response = client.get("/health", data={
        "status": "Flask",
    })
    assert response.status_code == 200
