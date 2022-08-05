from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, related_name='perfil', on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='foto_perfil')
    
