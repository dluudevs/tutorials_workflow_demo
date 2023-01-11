from django.test import TestCase
from django.urls import reverse
import pytest # no need to import pytest-django, pytests uses it automatically
from tutorials.models import Tutorial

# Create your tests here.
def test_homepage_access():
  url = reverse('home')
  assert url == "/"

# UNIT TESTS

# @pytest.mark.django_db # decorator tests access to the connected database
# def test_create_tutorial():
#   tutorial = Tutorial.objects.create(
#     title ='Pytest',
#     tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
#     description='Tutorial on how to apply pytest to a Django application',
#     published=True
#   )

#   assert tutorial.title == "Pytest"

@pytest.fixture # fixure is used to create data - here we're creating a tutorial object
def new_tutorial(db): # db param is built-in fixture provided by pytest-django. used by other fixture functions to get access to connected database
  tutorial = Tutorial.objects.create(
    title ='Pytest',
    tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
    description='Tutorial on how to apply pytest to a Django application',
    published=True
  )

  return tutorial

@pytest.fixture
def another_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='More-Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )

    return tutorial

# tests uses fixture function as parameter, fixture function runs firsrt when either of these tests are run
def test_search_tutorials(new_tutorial): 
  assert Tutorial.objects.filter(title='Pytest').exists()

def test_update_tutorial(new_tutorial):
  new_tutorial.title = 'Pytest-Django'
  new_tutorial.save()
  assert Tutorial.objects.filter(title='Pytest-Django').exists()

def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk # pk in Django ORM is primary key of database object
