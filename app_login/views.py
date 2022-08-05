
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def sign_up(request):
    form = UserCreationForm()
    registrado = False
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
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
    return HttpResponseRedirect(reverse('login:login'))
