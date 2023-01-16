import pytest
from api.integrations.abstract_method import PyPiAbstract
from api.integrations.client import PyPiClient


def test_pypi_is_subclass():
    assert issubclass(PyPiClient, PyPiAbstract)


@pytest.mark.vcr()
def test_pypi_package_metadata(pypi_client):
    package_name = "djangorestframework"

    response = pypi_client.package_metadata(package_name=package_name)

    assert sorted(response.keys()) == sorted(
        ["info", "last_serial", "releases", "urls", "vulnerabilities"]
    )
    assert response["info"]["version"] == "3.14.0"
    assert response["info"]["name"] == package_name


@pytest.mark.vcr()
def test_pypi_package_metadata_not_found(pypi_client):
    package_name = "notfoundpackage"

    response = pypi_client.package_metadata(package_name=package_name)

    assert response == {"message": "Not Found"}


@pytest.mark.vcr()
def test_pypi_package_metadata_by_version(pypi_client):
    package_name = "djangorestframework"
    version = "3.14.0"

    response = pypi_client.package_metadata_by_version(
        package_name=package_name,
        version=version,
    )

    assert sorted(response.keys()) == sorted(
        ["info", "last_serial", "urls", "vulnerabilities"]
    )
    assert response["info"]["version"] == version
    assert response["info"]["name"] == package_name


@pytest.mark.vcr()
def test_pypi_package_metadata_by_version_not_found(pypi_client):
    package_name = "notfoundpackage"
    version = "3.14.0"

    response = pypi_client.package_metadata_by_version(
        package_name=package_name,
        version=version,
    )

    assert response == {"message": "Not Found"}
