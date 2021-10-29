from django.db import models

# Create your models here.

class Proyecto(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    app_url = models.URLField(verbose_name='link_app', blank=True, null=True)
    github_url = models.URLField(verbose_name='link_github', blank=True, null=True)
    imagen = models.ImageField(upload_to="webapp", null=True, blank=True)   
    detalle = models.TextField()