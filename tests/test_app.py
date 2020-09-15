"""Integration tests for app.py"""
import pytest

from bank_api.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_account_creation(client):
    # Use the client to make requests e.g.:
    # client.post(...)
    # client.get(...)
    # https://flask.palletsprojects.com/en/1.1.x/testing/
    result = client.post('/accounts/new_account')
    assert result.status_code == 200
    assert result.json == {'name': 'new_account'}

    result = client.get('/accounts/new_account')
    assert result.status_code == 200
    assert result.json == {'name': 'new_account'}

    result = client.post('/accounts/new_account')
    assert result.status_code == 200
    assert result.json == {'name': 'new_account'}

    result = client.get('/accounts/unknown_account')
    assert result.status_code == 404
