from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    image = models.ImageField(upload_to='projects/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
