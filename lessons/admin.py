from django.contrib import admin

from lessons import models

# Register your models here.

admin.site.register(models.Student)
admin.site.register(models.Subject)
admin.site.register(models.Lecturer)
