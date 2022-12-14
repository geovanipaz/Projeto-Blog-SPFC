
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, TemplateView, \
    DeleteView
from .models import Blog, Categoria, Comentario, Gostei
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriaBlogForm, ComentarioForm
import uuid
from django.db.models import Q

# Create your views here.

def lista_blog(request, pk = None):
    blogs = Blog.objects.all()
    categorias = Categoria.objects.all()
    
    q = request.GET.get('busca')
    
    if pk:
        categoria = Categoria.objects.get(id=pk)
        blogs = blogs.filter(categoria=categoria)
    
    if q:
        blogs = blogs.filter(
            Q(blog_titulo__icontains=q)|
            Q(blog_conteudo__icontains=q)
        )
    context={
        'blogs': blogs,
        'categorias':categorias
        }
    return render(request,'app_blog/lista_blog.html', context)

def cria_blog(request):
    form = CriaBlogForm()
    if request.method == 'POST':
        form = CriaBlogForm(request.POST, request.FILES)
        if form.is_valid():
            obj_blog = form.save(commit=False)
            obj_blog.autor = request.user
            titulo = obj_blog.blog_titulo
            obj_blog.slug = titulo.replace(" ","-")+"-"+str(uuid.uuid4())
            obj_blog.save()
            return HttpResponseRedirect(reverse('blog:lista_blog'))
    context = {'form':form}
    return render(request, 'app_blog/cria_blog.html', context)

@login_required
def blog_detalhe(request, slug):
    blog = Blog.objects.get(slug=slug)
    form = ComentarioForm()
    ja_gostado = Gostei.objects.filter(blog=blog, usuario=request.user)
    if ja_gostado:
        gostado = True
    else:
        gostado = False
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.blog = blog
            comentario.save()
            return HttpResponseRedirect(reverse('blog:blog_detalhe', kwargs={'slug':slug}))
    context = {'blog':blog, 'form':form,'gostado':gostado}
    return render(request,'app_blog/blog_detalhe.html', context)

def gostar(request, pk):
    blog = Blog.objects.get(pk=pk)
    usuario = request.user
    ja_gostados = Gostei.objects.filter(blog=blog, usuario=usuario)
    if not ja_gostados:
        blog_gostado = Gostei(blog=blog, usuario=usuario)
        blog_gostado.save()
    return HttpResponseRedirect(reverse('blog:blog_detalhe', kwargs={'slug':blog.slug}))

def desgostar(request, pk):
    blog = Blog.objects.get(pk=pk)
    usuario = request.user
    ja_gostados = Gostei.objects.filter(blog=blog, usuario=usuario)
    ja_gostados.delete()
    return HttpResponseRedirect(reverse('blog:blog_detalhe', kwargs={'slug':blog.slug}))