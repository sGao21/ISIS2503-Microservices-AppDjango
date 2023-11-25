from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % (self.name)