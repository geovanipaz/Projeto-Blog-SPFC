from django.urls import path

from app_login import views

app_name = 'app_login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.pagina_login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('edita_perfil/', views.edita_usuario, name='edita_perfil')
]
