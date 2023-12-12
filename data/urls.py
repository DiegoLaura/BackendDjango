from django.urls import path
from .views import (
    UsuarioListCreateView,
    UsuarioDetailView,
    DiccionarioListCreateView,
    DiccionarioDetailView,
    PagoListCreateView,
    PagoDetailView,
    MembresiaListCreateView,
    MembresiaDetailView,
    ComentarioListCreateView,
    ComentarioDetailView,
    LoginView
)

urlpatterns = [
    path('usuarios/', UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'),
    
    path('diccionarios/', DiccionarioListCreateView.as_view(), name='diccionario-list-create'),
    path('diccionarios/<int:pk>/', DiccionarioDetailView.as_view(), name='diccionario-detail'),
    
    path('pagos/', PagoListCreateView.as_view(), name='pago-list-create'),
    path('pagos/<int:pk>/', PagoDetailView.as_view(), name='pago-detail'),
    
    path('membresias/', MembresiaListCreateView.as_view(), name='membresia-list-create'),
    path('membresias/<int:pk>/', MembresiaDetailView.as_view(), name='membresia-detail'),
    
    path('comentarios/', ComentarioListCreateView.as_view(), name='comentario-list-create'),
    path('comentarios/<int:pk>/', ComentarioDetailView.as_view(), name='comentario-detail'),

    path('login/', LoginView.as_view(), name='login'),

]
