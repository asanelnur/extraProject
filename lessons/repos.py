from typing import Protocol

from django.db.models import Count
from django.http import QueryDict

from lessons import models


class LessonRepositoryInterface(Protocol):

    @staticmethod
    def get_subjects() -> QueryDict[models.Subject]: ...

    @staticmethod
    def get_lecturers() -> QueryDict[models.Lecturer]: ...

    @staticmethod
    def get_students() -> QueryDict[models.Student]: ...


class LessonRepositoryV1:

    @staticmethod
    def get_subjects() -> QueryDict[models.Subject]:
        return models.Subject.objects.select_related('lecturer').annotate(
            total_students=Count('students')
        )

    @staticmethod
    def get_lecturers() -> QueryDict[models.Lecturer]:
        return models.Lecturer.objects.prefetch_related('subjects').annotate(
            total_subjects=Count('subjects')
        )

    @staticmethod
    def get_students() -> QueryDict[models.Student]:
        return models.Student.objects.prefetch_related('subjects').annotate(
            total_subjects=Count('subjects')
        )
