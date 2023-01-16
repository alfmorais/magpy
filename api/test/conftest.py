import pytest
import requests
from api.integrations.client import PyPiClient
from api.test._factories import PackageReleaseFactory, ProjectFactory
from pytest_factoryboy import register
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

register(ProjectFactory, "project")
register(PackageReleaseFactory, "package_release")


@pytest.fixture
def pypi_client():
    return PyPiClient(
        client=requests, user_agent="API-Instruct-Test-Python/1.0.0"
    )  # noqa E501


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def api_token(db, user):
    token, _ = Token.objects.get_or_create(user=user)
    return token


@pytest.fixture
def api_client_logged(db, api_client, api_token):
    api_client.credentials(HTTP_AUTHORIZATION="Token " + api_token.key)
    return api_client
