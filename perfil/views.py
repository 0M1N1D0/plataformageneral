from django.shortcuts import render
from .forms import CustomLoginForm


def login(request):
    form = CustomLoginForm(request.POST or None)


