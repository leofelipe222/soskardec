from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def registrar(request):
    # Register user
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuário já existe, tente novamente')
                return redirect('registrar')
            else:
                # Check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email já existe, tente novamente')
                    return redirect('registrar')
                else:
                    # Looks good, create the user
                    user = User.objects.create_user(username=username, password=password, email=email,
                    first_name=first_name, last_name=last_name)
                    # Login after register
                    auth.login(request, user)
                    messages.success(request, 'Registro concluído. Seja bem vindo(a)!')
                    return redirect('index')
                    # user.save()
                    # messages.success(request, 'Registro concluído. Seja bem vindo(a)!')
                    # return redirect('index')
        else:
            messages.error(request, 'As senhas não são iguais, tente novamente!')
            return redirect('registrar')
        
    else:
        return render(request, 'accounts/registrar.html')

def login(request):
    # Login user
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, ' - Você está logado(a)!')
            return redirect('painel_usuario')
        else:
            messages.error(request, 'Usuário ou Senha incorretos')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, " - Logout efetuado")
    return redirect('index')

def painel_usuario(request):
    return render(request, 'accounts/painel_usuario.html')
