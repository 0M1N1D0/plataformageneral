from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomLoginForm
from .forms import CustomUserCreationForm
from django.contrib import messages


def login(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CustomLoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                # login user and redirect to home page
                login(request, user)
                return redirect('home')
            # redirect to a new URL:
        return render(request, "login.html", {"form": form})
    
        

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomLoginForm()
        return render(request, "perfil/login.html", {"form": form})
    

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu cuenta ha sido creada exitosamente! Por favor, inicia sesión para continuar.')
            return redirect('perfil:login')
    else:
        form = CustomUserCreationForm()
        if form.errors:
            messages.success(request, 'Algo salió mal. Por favor, intente de nuevo.')
    return render(request, 'perfil/registro.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


   


