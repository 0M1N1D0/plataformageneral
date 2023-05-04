"""
Para modificar el formulario de login de Django y hacer que solicite el número de nómina en lugar del nombre de usuario, debes crear un formulario personalizado que herede de AuthenticationForm, la cual es la clase que representa el formulario de inicio de sesión predeterminado en Django.

Para hacer esto, debes crear un archivo forms.py 
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm, authenticate

class CustomLoginForm(AuthenticationForm):
    numero_nomina = forms.IntegerField(label="Número de nómina")

    error_messages = {
        'invalid_login': "Por favor, ingrese un número de nómina y contraseña correctos. Note que ambos campos pueden ser sensibles a mayúsculas y minúsculas."
    }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.pop('autofocus', None)
    #     self.fields['password'].widget.attrs.pop('autocomplete', None)

    #     # Renombrar la etiqueta del campo username a "Número de nómina"
    #     self.fields['username'].label = "Número de nómina"

    #     # Hacer que el campo username sea requerido y eliminar el campo username
    #     self.fields['username'].required = True
    #     del self.fields['username']

    # def clean(self):
    #     numero_nomina = self.cleaned_data.get('numero_nomina')
    #     password = self.cleaned_data.get('password')

    #     if numero_nomina is not None and password:
    #         self.user_cache = authenticate(numero_nomina=numero_nomina, password=password)
    #         if self.user_cache is None:
    #             raise self.get_invalid_login_error()
    #         else:
    #             self.confirm_login_allowed(self.user_cache)
    #     return self.cleaned_data