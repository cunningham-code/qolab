from django.db import models


class Timer(models.Model):
    code = models.CharField(max_length=6)
    start = models.CharField(max_length=2000)
    end = models.CharField(max_length=2000)
    day = models.CharField(max_length=2000)
    names = models.CharField(max_length=20000, default="Name")
    emails = models.CharField(max_length=20000, default="")
    youtube = models.CharField(max_length=200, default="youtube.com")

    def __str__(self):
        return self.start
