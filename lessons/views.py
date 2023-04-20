from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from lessons import models, serializers, filters, services


# Create your views here.


class SubjectViewSet(viewsets.ModelViewSet):
    lesson_service = services.LessonServiceV1()
    queryset = lesson_service.get_subjects()
    serializer_class = serializers.SubjectSerializer
    filter_backends =(DjangoFilterBackend,)
    filterset_class = filters.SubjectFilter



class LecturerViewSet(viewsets.ModelViewSet):
    lesson_service = services.LessonServiceV1()
    queryset = lesson_service.get_lecturers()
    serializer_class = serializers.LecturerSerializer


class StudentViewSet(viewsets.ModelViewSet):
    lesson_service = services.LessonServiceV1()
    queryset = lesson_service.get_students()
    serializer_class = serializers.StudentSerializer
