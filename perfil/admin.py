from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     list_display = (
#         'username', 
#         'nombres', 
#         'apellido_paterno', 
#         'apellido_materno', 
#         'numero_nomina', 
#         'email', 
#         'supervisor', 
#         'is_admin'
#     )

admin.site.register(CustomUser, UserAdmin)