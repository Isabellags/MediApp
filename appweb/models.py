from django.db import models

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
