from django.db import models
from django.utils.translation import activate

# Create your models here.


#la caracteristicas que tendra nuestro inmuebles

class Inmueble(models.Model):
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    imagen = models.CharField(max_length=900)
    activo = models.BooleanField(default=True)
    
    
    #indicar cual va ser el indice
    
    def __str__(self):
        return self.direccion