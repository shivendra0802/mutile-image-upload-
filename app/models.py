from django.db import models

# Create your models here.
class Multiple(models.Model):
    images = models.FileField()

    # def __str__(self):
    #     return self.images

class Danger(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name