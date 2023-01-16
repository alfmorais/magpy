from api.usercases.abstract_method import ParsePackageAbstract


class ParsePackage(ParsePackageAbstract):
    def __init__(self, client, packages):
        self.client = client
        self.packages = packages
        self.validated_packages = []

    def _validate_package_name(self, package):
        try:
            name = package["name"]
        except KeyError:
            # TODO: raise validation error:
            pass
        else:
            return name

    def _validate_package_version(self, package):
        try:
            version = package["version"]
        except KeyError:
            version = None
        else:
            return version

    def _validade_package_response(self, package_info):
        if package_info == {"message": "Not Found"}:
            raise ValueError

        try:
            name = package_info["info"]["name"]
            version = package_info["info"]["version"]
        except KeyError:
            raise ValueError
        else:
            return {"name": name, "version": version}

    def get_packages_on_pypi(self):
        for package in self.packages:
            name = self._validate_package_name(package)
            version = self._validate_package_version(package)

            if version is None:
                package_info = self.client.package_metadata(package_name=name)

                validated_package = self._validade_package_response(
                    package_info=package_info
                )

                self.validated_packages.append(validated_package)

            if version:
                package_info = self.client.package_metadata_by_version(
                    package_name=name, version=version
                )

                validated_package = self._validade_package_response(
                    package_info=package_info
                )

                self.validated_packages.append(validated_package)

        return self.validated_packages
