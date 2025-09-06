import pytest
from Yougile import Yougile
import time
import random
import string
import requests


@pytest.fixture
def api_client():
    client = Yougile()
    return client

# Позитивные тесты
def test_create_project_positive(api_client):
    title = f"Test Project {int(time.time())} {random.choice(string.ascii_letters)}"
    response = api_client.create_project(title)
    assert response.status_code == 201
    assert "id" in response.json()


def test_update_project_positive(api_client):
    title = f"Test Project {int(time.time())} {random.choice(string.ascii_letters)}"
    create_response = api_client.create_project(title)
    assert create_response.status_code == 201
    project_id = create_response.json()["id"]

    # Обновим проект
    new_title = f"Updated {title}"
    update_response = api_client.update_project(project_id, new_title)
    assert update_response.status_code == 200
    data = update_response.json()


def test_get_projects_positive(api_client):
    response = api_client.get_projects()
    assert response.status_code == 200
    data = response.json()
    assert "content" in data
    assert isinstance(data["content"], list)


# Негативные тесты
def test_create_project_negative_invalid_token(api_client):
    api_client.auth_token = "invalid_token"
    title = f"Test Project {int(time.time())}"
    response = api_client.create_project(title)
    assert response.status_code == 401

def test_update_project_negative_not_found(api_client):
    project_id = "nonexistent_id"
    title = "Updated Title"
    response = api_client.update_project(project_id, title)
    assert response.status_code == 404


def test_get_projects_negative(api_client):
    api_client_invalid = Yougile()
    url = f"{api_client_invalid.base_url}/projects"
    response = requests.get(url)
    assert response.status_code in [401]



