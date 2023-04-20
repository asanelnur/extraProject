from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)

    def __str__(self):
        return f'{self.id}: {self.title}'

