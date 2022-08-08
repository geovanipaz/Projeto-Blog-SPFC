
from dataclasses import fields

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from app_login.models import Perfil

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        
class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password')
        
class FotoPerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto_perfil',]