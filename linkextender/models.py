from django.db import models

# Create your models here.
class ExtendedLink(models.Model):
    url = models.URLField()
    longlink = models.TextField()
    segments = models.IntegerField()

    def __str__(self):
        return f"/{self.longlink} pointing to {self.url} with {self.segments} segments"