from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cargo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Profesional(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    especialista = models.BooleanField()
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(default='')

    def __str__(self):
        return self.rut
    
lista_tipo_contacto = [
    [0, "Sugerencia"],
    [1, "Reclamo"],
    [2, "Felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    tipo_contacto = models.IntegerField(choices=lista_tipo_contacto)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre + " "+self.email
    
# models.py


class FormularioContacto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    # Otros campos del formulario si es necesario






