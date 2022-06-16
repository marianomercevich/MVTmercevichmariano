from django.db import models

class Familiar(models.Model):

    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    fecha_de_nacimento = models.DateField (blank=True, null=True)
    edad = models.IntegerField ()
    email = models.EmailField(blank=True, null=True)
    telefono = models.IntegerField()

