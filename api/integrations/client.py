from api.integrations.abstract_method import PyPiAbstract


class PyPiClient(PyPiAbstract):
    def __init__(self, client, user_agent):
        self.client = client
        self.headers = {"user-agent": user_agent}

    def package_metadata(self, package_name):
        URL = f"https://pypi.org/pypi/{package_name}/json"

        response = self.client.get(URL, headers=self.headers)
        return response.json()

    def package_metadata_by_version(self, package_name, version):
        URL = f"https://pypi.org/pypi/{package_name}/{version}/json"

        response = self.client.get(URL, headers=self.headers)
        return response.json()
