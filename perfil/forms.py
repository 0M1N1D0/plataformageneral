"""
Para modificar el formulario de login de Django y hacer que solicite el número de nómina en lugar del nombre de usuario, debes crear un formulario personalizado que herede de AuthenticationForm, la cual es la clase que representa el formulario de inicio de sesión predeterminado en Django.

Para hacer esto, debes crear un archivo forms.py 
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.forms.widgets import CheckboxInput  
from django.forms.widgets import TextInput


class CustomLoginForm(AuthenticationForm):
    username = forms.IntegerField(label="Usuario")

    error_messages = {
        'invalid_login': "Por favor, ingrese un número de nómina y contraseña correctos. Note que ambos campos pueden ser sensibles a mayúsculas y minúsculas."
    }

   
   
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # agrega campos personalizados al formulario
        fields = UserCreationForm.Meta.fields + ('nombres','apellido_paterno','apellido_materno','numero_nomina','email','supervisor','is_staff', 'is_superuser')

    # agregar clases de bootstrap a los campos del formulario
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            # elimina las etiquetas de los campos
            self.fields[field].label = ''

        # Agregar clases CSS a los campos del formulario
        self.fields['username'].widget.attrs.update({'placeholder': 'Usuario'})
        self.fields['nombres'].widget.attrs.update({'placeholder': 'Nombre(s)'})
        self.fields['apellido_paterno'].widget.attrs.update({'placeholder': 'Apellido Paterno'})
        self.fields['apellido_materno'].widget.attrs.update({'placeholder': 'Apellido Materno'})
        self.fields['numero_nomina'].widget.attrs.update({'placeholder': 'Número de Nómina'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Correo Electrónico'})
        self.fields['supervisor'].widget.attrs.update({'placeholder': 'Supervisor'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirmar Contraseña'})
        self.fields['is_staff'].widget = CheckboxInput(attrs={'class': 'form-check-input'})
        self.fields['is_superuser'].widget = CheckboxInput(attrs={'class': 'form-check-input'})

