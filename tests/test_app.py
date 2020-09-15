"""Integration tests for app.py"""
import pytest
from bank_api.bank import Bank
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


def test_get_unknown_account(client):
    result = client.get('/accounts/unknown_account')
    assert result.status_code == 404

@pytest.fixture
def bank() -> Bank:
    return Bank()

def test_add_money(client, bank):
    bank.create_account('new_account')
    result = client.post('/accounts/money', json={
        "name": "new_account",
        "amount": 1
    })
    assert result.status_code == 200
