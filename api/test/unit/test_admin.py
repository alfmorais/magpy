def test_admin_project(admin_client, project):
    url = "/admin/api/project/"

    response = admin_client.get(url)
    assert response.status_code == 200


def test_admin_package_release(admin_client, package_release):
    url = "/admin/api/packagerelease/"

    response = admin_client.get(url)
    assert response.status_code == 200
