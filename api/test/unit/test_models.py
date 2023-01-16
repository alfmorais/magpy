import uuid

import pytest

pytestmark = pytest.mark.django_db


def test_project_string_method(project):
    project.name = "CleanCode"

    assert str(project) == "CleanCode"


def test_project_release_string_method(package_release):
    package_release.name = "CleanCode"
    package_release.version = "1.0.0"

    assert str(package_release) == "CleanCode 1.0.0"


def test_project_fields(project):
    assert type(project.id) == uuid.UUID
    assert type(project.name) == str


def test_package_release_fields(package_release, project):
    assert type(package_release.id) == uuid.UUID
    assert type(package_release.name) == str
    assert type(package_release.version) == str
    assert package_release.project == project
