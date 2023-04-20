from django_filters import rest_framework as filters

from lessons import models


class SubjectFilter(filters.FilterSet):
    credits = filters.NumberFilter(field_name='credits', lookup_expr='gte')
    first_name = filters.CharFilter(field_name='lecturer__first_name')
    student_name = filters.CharFilter(field_name='students__first_name')

    class Meta:
        model = models.Subject
        fields = ('lecturer', 'students')
