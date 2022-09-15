from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=400)

    def __str__(self):
        return str(self.title)