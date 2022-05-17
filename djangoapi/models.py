from django.db import models

class Entrada (models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    imagen=models.ImageField(upload_to='documents/images/')

    def __str__(self):
        return self.title