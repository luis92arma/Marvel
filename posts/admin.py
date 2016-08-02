from django.contrib import admin
from .models import Post, Comentario
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'slug',
        'status',
        'creado',
    )
    list_filter = ('status', 'creado', 'actualizado')
    search_fields = ('titulo', 'cuerpo', 'creado', 'slug')
    prepopulated_fields = {'slug':('titulo',)}
    date_hierchy = 'creado'
    ordering = ['status', 'creado']

class ComentarioAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'autor',
        'email',
        'fecha',
        'activo',
    )
    list_filter = ('post','fecha', 'activo')
    search_fields = ('post','fecha', 'titulo')
    ordering = ['fecha']

admin.site.register(Post, PostAdmin)
admin.site.register(Comentario, ComentarioAdmin)
