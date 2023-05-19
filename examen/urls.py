from django.urls import path
from . import views


app_name = 'examen'

urlpatterns = [
    path('consulta/', views.consulta, name='consulta'),
    path('aplicacion/', views.aplicacion, name='aplicacion'),
]