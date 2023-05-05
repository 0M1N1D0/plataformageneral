"""
Para modificar el formulario de login de Django y hacer que solicite el número de nómina en lugar del nombre de usuario, debes crear un formulario personalizado que herede de AuthenticationForm, la cual es la clase que representa el formulario de inicio de sesión predeterminado en Django.

Para hacer esto, debes crear un archivo forms.py 
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.forms.widgets import CheckboxInput  

class CustomLoginForm(AuthenticationForm):
    username = forms.IntegerField(label="Usuario")

    error_messages = {
        'invalid_login': "Por favor, ingrese un número de nómina y contraseña correctos. Note que ambos campos pueden ser sensibles a mayúsculas y minúsculas."
    }

   
   
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('nombres','apellido_paterno','apellido_materno','numero_nomina','email','supervisor','is_staff', 'is_superuser')

    # agregar clases de bootstrap a los campos del formulario
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        # Agregar clases CSS a los campos is_staff y is_superuser
        self.fields['is_staff'].widget = CheckboxInput(attrs={'class': 'form-check-input'})
        self.fields['is_superuser'].widget = CheckboxInput(attrs={'class': 'form-check-input'})
