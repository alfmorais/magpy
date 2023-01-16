from abc import ABC


class PyPiAbstract(ABC):
    def __init__(self, client, user_agent):
        self.client = client
        self.headers = {"user-agent": user_agent}

    def package_metadata(self):
        pass

    def package_metadata_by_version(self):
        pass
