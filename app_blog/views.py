from django.shortcuts import render

# Create your views here.

def lista_blog(request):
    return render(request,'app_blog/lista_blog.html', context={})
