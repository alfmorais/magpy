import uuid

import factory
from api.test._factories.project import ProjectFactory


class PackageReleaseFactory(factory.django.DjangoModelFactory):
    id = uuid.uuid4()
    name = factory.Faker("name")
    version = factory.Faker("name")
    project = factory.SubFactory(ProjectFactory)

    class Meta:
        model = "api.PackageRelease"
