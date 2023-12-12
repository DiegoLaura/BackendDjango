from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)

class Diccionario(models.Model):
    imagen = models.ImageField(upload_to='diccionario/')
    descripcion = models.TextField()

class Pago(models.Model):
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    dni = models.IntegerField()
    celular = models.IntegerField()
    estado = models.CharField(max_length=1)

class Membresia(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    estado = models.CharField(max_length=255)
    tiempo = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

class Comentario(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    celular = models.IntegerField()
    comentario = models.TextField()
