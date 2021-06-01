from django.db import models


class HeadLines(models.Model):
    title = models.CharField(max_length=250)
    office = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = '-created'
