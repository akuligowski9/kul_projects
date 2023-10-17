from django.db import models


# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.name


class Scene(models.Model):
    title = models.CharField(max_length=50)
    grouping = models.CharField(max_length=20)

    def __str__(self):
        return self.title
