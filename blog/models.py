from django.db import models

# Create your models here.


class MyModelName(models.Model):
    """
    Una clase típica definiendo un modelo, derivado desde la clase Model.
    """

    # Campos
    nombre= models.CharField(max_length=20, help_text="Enter field documentation")



    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return self.nombre