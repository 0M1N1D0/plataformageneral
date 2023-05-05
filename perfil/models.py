from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    nombres = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    numero_nomina = models.IntegerField(primary_key=True, verbose_name="Número de nómina")
    email = models.EmailField(unique=True)
    supervisor = models.CharField(max_length=50)

    def __str__(self):
        return self.nombres + " " + self.apellido_paterno + " " + self.apellido_materno
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["numero_nomina"]


