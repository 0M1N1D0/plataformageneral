from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'nombres', 'apellido_paterno', 'apellido_materno', 'numero_nomina', 'email', 'supervisor', 'is_staff'),
        }),
    )

    list_display = ('username', 'nombres', 'apellido_paterno', 'apellido_materno', 'numero_nomina', 'email', 'supervisor', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)


