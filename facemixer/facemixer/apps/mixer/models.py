from django.db import models


class Photo(models.Model):
    photo = models.ImageField(upload_to='media', null=True)
    photo_rating = models.PositiveIntegerField(default=1400, null=True)
    pub_date = models.DateTimeField(null=True)

    def __str__(self):
        return "Rating={0}".format(self.photo_rating)
