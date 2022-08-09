from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Comentario, Blog, Categoria, Gostei

class CriaBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('blog_titulo', 'categoria', 'blog_conteudo', 'blog_imagem')