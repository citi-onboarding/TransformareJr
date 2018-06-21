from django.db import models

# Create your models here.

class mvv(models.Model):
    missao = models.TextField()
    visao = models.TextField()
    valores = models.TextField()