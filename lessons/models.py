from django.db import models

# Create your models here.


class Lecturer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True)
    salary = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    # student = models.OneToOneField('Student', on_delete=models.PROTECT, related_name='adviser', null=True)

    def __str__(self):
        return self.first_name


class Subject(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    credits = models.PositiveIntegerField()
    lecturer = models.ForeignKey(to=Lecturer, on_delete=models.CASCADE, related_name='subjects', null=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    subjects = models.ManyToManyField(to=Subject, related_name='students')

    def __str__(self):
        return self.first_name
