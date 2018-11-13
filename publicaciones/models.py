from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.text import slugify

# Create your c

class Titulare(models.Model):
    titulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to = 'foto/',blank=True)
    texto = models.TextField(max_length=500)
    creado = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    def __str__(self):
        titulo = str(self.titulo)
        return titulo
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Titulare, self).save(*args, **kwargs)

class Articulo(models.Model):
    titulo = models.ForeignKey(Titulare, on_delete=models.CASCADE)
    subtitulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to = 'foto/',blank=True)
    texto = models.TextField()
    creado = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    def __str__(self):
        titulo = str(self.titulo)
        return titulo
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Articulo, self).save(*args, **kwargs)



