import pytest
from flask import session

@pytest.fixture()
def test_registration(client):
    with client:
        client.post("/register")
        # session is still accessible
        assert session["username"] == form.username.data

@pytest.fixture()
def test_login(client):
    with client:
        client.post("/login")
        # session is still accessible
        assert session["username"] == form.username.data

@pytest.fixture()
def test_search_for_hotel(client):
    with client:
        client.post("/search_for_hotel")
        # session is still accessible
        assert session["city"] == form.city.data

@pytest.fixture()
def test_display_rates(client):
    with client:
        client.post("/display_rates")
        # session is still accessible
        assert session["check_in_date"] == form.check_in_date.data
