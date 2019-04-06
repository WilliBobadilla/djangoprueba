from django.db import models
from django.utils import timezone


class Post(models.Model): #heredamos de los models, creando un objeto post
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)  #longitud maxima de 200 caracteres
    text = models.TextField()               # campo de texto 
    created_date = models.DateTimeField(
            default=timezone.now)   #fecha de la entrada 
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title