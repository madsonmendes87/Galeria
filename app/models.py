from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.TextField(max_length=255)
    senha = models.TextField(max_length=255)
    casal = models.CharField(max_length=1)
