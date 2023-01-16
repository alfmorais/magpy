import requests
from api.integrations.client import PyPiClient
from api.usercases.parse_package import ParsePackage
from rest_framework import serializers

from .models import PackageRelease, Project


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRelease
        fields = ["name", "version"]
        extra_kwargs = {"version": {"required": False}}


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["name", "packages"]

    packages = PackageSerializer(many=True)

    def _validate_packages(self, parse_packages):
        try:
            packages = parse_packages.get_packages_on_pypi()
        except (KeyError, ValueError):
            message = {"error": "One or more packages doesn't exist"}

            raise serializers.ValidationError(detail=message, code=400)
        else:
            return packages

    def create(self, validated_data):
        project_name = validated_data["name"]
        packages = validated_data["packages"]

        client = PyPiClient(
            client=requests, user_agent="API-Instruct-Test-Python/1.0.0"
        )

        parse_package = ParsePackage(client=client, packages=packages)

        packages = self._validate_packages(parse_package)

        project = Project.objects.create(name=project_name)

        for package in packages:
            PackageRelease.objects.create(project=project, **package)

        return project
