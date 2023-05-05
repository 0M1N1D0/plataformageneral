from django.db import models
from django.contrib.auth.models import AbstractUser


class Supervisor(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre del supervisor")
    apellido_paterno = models.CharField(max_length=50, verbose_name="Apellido paterno del supervisor")
    apellido_materno = models.CharField(max_length=50, verbose_name="Apellido materno del supervisor")

    def __str__(self):
        return self.nombre + " " + self.apellido_paterno + " " + self.apellido_materno
    
    class Meta:
        verbose_name = "Supervisor"
        verbose_name_plural = "Supervisores"
        ordering = ["nombre"]


class CustomUser(AbstractUser):
    nombres = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    numero_nomina = models.IntegerField(primary_key=True, verbose_name="Número de nómina")
    email = models.EmailField(unique=True)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, verbose_name="Supervisor")

    def __str__(self):
        return self.nombres + " " + self.apellido_paterno + " " + self.apellido_materno
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["numero_nomina"]


