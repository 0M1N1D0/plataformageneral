# from django.db import models
# from django.contrib.auth.models import AbstractUser


# class CustomUser(AbstractUser):
#     nombres = models.CharField(max_length=50)
#     apellido_paterno = models.CharField(max_length=50)
#     apellido_materno = models.CharField(max_length=50)
#     numero_nomina = models.IntegerField(primary_key=True)
#     email = models.EmailField(unique=True)
#     supervisor = models.CharField(max_length=50)
#     is_admin = models.BooleanField(default=False)


#     # ********************************************************************
#     # Agregar related_name a las relaciones de clave externa inversas
#     # para solucionar el error de ambigüedad al hacer migraciones
#     groups = models.ManyToManyField(
#         "auth.Group",
#         related_name="custom_users",
#         blank=True,
#         help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
#         verbose_name="groups",
#     )

#     user_permissions = models.ManyToManyField(
#         "auth.Permission",
#         related_name="custom_users",
#         blank=True,
#         help_text="Specific permissions for this user.",
#         verbose_name="user permissions",
#     )
#     # ********************************************************************