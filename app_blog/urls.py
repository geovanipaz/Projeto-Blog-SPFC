from django.urls import path

from app_blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.lista_blog, name='lista_blog'),
    path('categoria/<pk>/', views.lista_blog, name='lista_por_categoria'),
    path('cria_blog/', views.cria_blog, name='cria_blog'),
    path('<slug>/', views.blog_detalhe, name='blog_detalhe')
]