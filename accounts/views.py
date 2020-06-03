from django.shortcuts import render, redirect

# Create your views here.
def registrar(request):
    return render(request, 'accounts/registrar.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect(request, 'index')

def usuario(request):
    return render(request, 'accounts/usuario.html')
