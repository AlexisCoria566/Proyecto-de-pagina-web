from django.db import models

# Create your models here.

class Opinion (models.Model):
    nombre=models.CharField(max_length=200,verbose_name="Usuario")
    comentario=models.TextField(verbose_name="Comentario")
    imagen=models.ImageField(verbose_name="Imagen de Perfil", upload_to="opinion")
    calificacion=models.ImageField(verbose_name="Calificacion", upload_to="opinion")
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Opinion"
        verbose_name_plural="Opiniones"
        ordering=["nombre"]

    def __str__(self):
        return self.nombre