
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app_login.forms import SignUpForm, UserProfileChange, FotoPerfilForm
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
    
@login_required
def muda_senha(request):
    usuario_atual = request.user
    mudada = False
    form = PasswordChangeForm(usuario_atual)
    if request.method == 'POST':
        form = PasswordChangeForm(usuario_atual, data=request.POST)
        if form.is_valid():
            form.save()
            mudada = True
    return render(request, 'app_login/muda_senha.html', context={
        'form':form, 'mudada':mudada})
    
@login_required
def adiciona_foto_perfil(request):
    form = FotoPerfilForm()
    if request.method == 'POST':
        form = FotoPerfilForm(request.POST, request.FILES)
        if form.is_valid():
            usuario_obg = form.save(commit=False)
            usuario_obg.usuario = request.user
            usuario_obg.save()
            return HttpResponseRedirect(reverse('app_login:perfil'))
    return render(request,'app_login/adiciona_foto_perfil.html',
                  context={'form':form})
    
@login_required
def mudar_foto_perfil(request):
    form = FotoPerfilForm(instance=request.user.perfil)
    if request.method == 'POST':
        form = FotoPerfilForm(
            request.POST, request.FILES, instance=request.user.perfil
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app_login:perfil'))
    return render(request,'app_login/adiciona_foto_perfil.html',
                  context={'form':form})