from django.urls import path

from app_login import views

app_name = 'login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.pagina_login, name='login'),
    path('logout/', views.logout_user, name='logout')
]
