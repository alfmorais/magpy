from abc import ABC


class ParsePackageAbstract(ABC):
    def __init__(self, client, packages):
        self.client = client
        self.packages = packages
        self.validated_packages = []

    def _validate_package_name(self):
        pass

    def _validate_package_version(self):
        pass

    def _validade_package_response(self):
        pass

    def get_packages_on_pypi(self):
        pass
