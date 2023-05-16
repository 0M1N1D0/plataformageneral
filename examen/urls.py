from django.urls import path
from . import views


app_name = 'examen'

urlpatterns = [
    path('aplicacion/', views.aplicacion, name='aplicacion'),
]