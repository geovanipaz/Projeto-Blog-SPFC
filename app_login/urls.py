from django.urls import path

from app_login import views

app_name = 'app_login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.pagina_login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('edita_perfil/', views.edita_usuario, name='edita_perfil'),
    path('muda_senha/', views.muda_senha, name='muda_senha'),
    path('add_foto_perfil/', views.adiciona_foto_perfil, name='add_foto_perfil'),
    path('mudar_foto_perfil/', views.mudar_foto_perfil, name='trocar_foto_perfil')
    
]
