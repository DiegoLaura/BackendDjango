from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import Usuario, Diccionario, Pago, Membresia, Comentario
from .serializers import UsuarioSerializer, DiccionarioSerializer, PagoSerializer, MembresiaSerializer, ComentarioSerializer
from django.http import JsonResponse
from rest_framework.views import APIView



class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class DiccionarioListCreateView(generics.ListCreateAPIView):
    queryset = Diccionario.objects.all()
    serializer_class = DiccionarioSerializer

class DiccionarioDetailView(generics.RetrieveAPIView):
    queryset = Diccionario.objects.all()
    serializer_class = DiccionarioSerializer

class PagoListCreateView(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class PagoDetailView(generics.RetrieveAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class MembresiaListCreateView(generics.ListCreateAPIView):
    queryset = Membresia.objects.all()
    serializer_class = MembresiaSerializer

class MembresiaDetailView(generics.RetrieveAPIView):
    queryset = Membresia.objects.all()
    serializer_class = MembresiaSerializer

class ComentarioListCreateView(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class ComentarioDetailView(generics.RetrieveAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        nombre = request.data.get('nombre')
        contrasena = request.data.get('contrasena')
        user = Usuario.objects.filter(nombre=nombre, contrasena=contrasena).first()

        if user is not None:
            # Serializa los datos del usuario y los devuelve
            user_data = UsuarioSerializer(user).data
            return JsonResponse({'success': True, 'user': user_data})
        else:
            return JsonResponse({'success': False, 'error': 'Credenciales inválidas'}, status=401)
