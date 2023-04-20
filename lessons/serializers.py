from rest_framework import serializers

from lessons import models


class _LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lecturer
        fields = ('first_name',)


class _StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ('id', 'first_name', 'last_name')



class SubjectSerializer(serializers.ModelSerializer):
    lecturer = _LecturerSerializer(read_only=True)
    students = _StudentSerializer(read_only=True, many=True)
    total_students = serializers.IntegerField()
    # students = _StudentSerializer(read_only=True, many=True)

    class Meta:
        model = models.Subject
        fields = ('title', 'credits', 'lecturer', 'total_students', 'students')


class LecturerSerializer(serializers.ModelSerializer):
    total_subjects = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.Lecturer
        fields = '__all__'



class StudentSerializer(serializers.ModelSerializer):
    total_subjects = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.Student
        fields = '__all__'
