from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('app_blog.urls')),
    path('account/', include('app_login.urls')),
    
]