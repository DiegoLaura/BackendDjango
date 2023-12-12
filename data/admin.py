# En data/admin.py
from django.contrib import admin
from .models import Usuario, Diccionario, Pago, Membresia, Comentario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'correo']

@admin.register(Diccionario)
class DiccionarioAdmin(admin.ModelAdmin):
    list_display = ['imagen', 'descripcion']

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'apellidos', 'dni', 'celular', 'estado']

@admin.register(Membresia)
class MembresiaAdmin(admin.ModelAdmin):
    list_display = ['id_usuario', 'id_pago', 'estado', 'tiempo', 'fecha_inicio', 'fecha_fin']

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'correo', 'celular', 'comentario']
