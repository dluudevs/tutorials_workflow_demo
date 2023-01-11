from django.test import TestCase
from django.urls import reverse
import pytest

# Create your tests here.
@pytest.fixture
def test_user(db, django_user_model): # django_user_model is built in fixture. short cut to User model for this project
    django_user_model.objects.create_user(
        username="test_username", password="test_password")
    return "test_username", "test_password"   # this returns a tuple

# integration test - between web client and django
def test_login_user(client, test_user): # client is a dummy web client provided by django
    test_username, test_password = test_user  # this unpacks the tuple
    login_result = client.login(username=test_username, password=test_password)
    assert login_result == True