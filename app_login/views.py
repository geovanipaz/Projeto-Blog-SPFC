
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app_login.forms import SignUpForm, UserProfileChange
# Create your views here.


def sign_up(request):
    form = SignUpForm()
    registrado = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registrado = True
    context = {'form':form,'registrado': registrado}
    return render(request, 'app_login/signup.html', context)

def pagina_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('blog:lista_blog'))
    
    return render(request, 'app_login/login.html', context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_login:login'))

@login_required
def perfil(request):
    return render(request,'app_login/perfil.html', context={})

@login_required
def edita_usuario(request):
    usuario_atual = request.user
    form = UserProfileChange(instance=usuario_atual)
    if request.method =='POST':
        form = UserProfileChange(request.POST, instance=usuario_atual)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=usuario_atual)
    return render(request,'app_login/edita_perfil.html', context={'form':form})
    