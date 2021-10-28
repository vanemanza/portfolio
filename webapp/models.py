from django.db import models

class Persona(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    foto = models.ImageField(upload_to='webapp', null=True, blank=True, height_field=None, width_field=None)
    about_me = models.TextField()

    def __str__(self):     
        fullname = f'{self.nombre} {self.apellido}'       
        return fullname