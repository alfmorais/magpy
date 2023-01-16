import uuid

import factory


class ProjectFactory(factory.django.DjangoModelFactory):
    id = uuid.uuid4()
    name = factory.Faker("name")

    class Meta:
        model = "api.Project"
