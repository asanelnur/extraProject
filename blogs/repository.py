from typing import Protocol, OrderedDict

from django.db.models import QuerySet

from blogs import models


class BlogRepositoriesInterface(Protocol):

    def create_blog(self, data: OrderedDict) -> models.Blog: ...

    def get_blogs(self) -> QuerySet[models.Blog]: ...


class BlogRepositoriesV1:
    model = models.Blog

    def create_blog(self, data: OrderedDict) -> models.Blog:
        return self.model.objects.create(**data)

    def get_blogs(self) -> QuerySet[models.Blog]:
        return self.model.objects.all()
