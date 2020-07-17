from django.db import models


# Create your models here.

class Foto(models.Model):
    foto_title = models.CharField(max_length=50)
    foto_rating = models.PositiveIntegerField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return "Rating={0}".format(self.foto_rating)
