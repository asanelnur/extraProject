from typing import Protocol

from django.http import QueryDict

from lessons import models, repos


class LessonServiceInterface(Protocol):
    lesson_repos: repos.LessonRepositoryInterface

    def get_subjects(self,) -> QueryDict[models.Subject]: ...

    def get_lecturers(self,) -> QueryDict[models.Lecturer]: ...

    def get_students(self,) -> QueryDict[models.Student]: ...


class LessonServiceV1:
    lesson_repos: repos.LessonRepositoryInterface = repos.LessonRepositoryV1()

    def get_subjects(self,) -> QueryDict[models.Subject]:
        return self.lesson_repos.get_subjects()

    def get_lecturers(self,) -> QueryDict[models.Lecturer]:
        return self.lesson_repos.get_lecturers()

    def get_students(self,) -> QueryDict[models.Student]:
        return self.lesson_repos.get_students()
