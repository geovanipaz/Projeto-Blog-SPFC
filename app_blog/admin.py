from django.contrib import admin
from .models import Blog, Comentario, Gostei, Categoria
# Register your models here.

admin.site.register(Blog)
admin.site.register(Comentario)
admin.site.register(Gostei)
admin.site.register(Categoria)
