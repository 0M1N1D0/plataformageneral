from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'perfil'

urlpatterns = [
    path('', LoginView.as_view(template_name='perfil/login.html'), name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_view, name='logout'),
]
