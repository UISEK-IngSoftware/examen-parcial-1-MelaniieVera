from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(help_text="Duración en minutos")
    genre = models.CharField(max_length=100)
    synopsis = models.TextField()
    image_filename = models.CharField(
        max_length=100,
        blank=True,
        help_text="Nombre del archivo de imagen en static/pelisflix/img/"
    )

    def __str__(self):
        return f"{self.title} ({self.release_year})"
