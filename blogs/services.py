from typing import Protocol, OrderedDict

from django.db.models import QuerySet

from blogs import models, repository


class BlogServicesInterface(Protocol):
    repos: repository.BlogRepositoriesInterface
    def create_blog(self, data: OrderedDict) -> models.Blog: ...

    def get_blogs(self) -> QuerySet[models.Blog]: ...


class BlogServicesV1:
    repos: repository.BlogRepositoriesInterface = repository.BlogRepositoriesV1()

    def create_blog(self, data: OrderedDict) -> models.Blog:
        print('create blog in service layer')
        return self.repos.create_blog(data=data)

    def get_blogs(self) -> QuerySet[models.Blog]:
        print('get blog in service layer')
        return self.repos.get_blogs()