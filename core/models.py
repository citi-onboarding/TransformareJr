from django.db import models

# Create your models here.

class editavei(models.Model):
    missao = models.TextField()
    visao = models.TextField()
    valores = models.TextField()
    email = models.TextField()
    telefone = models.TextField()