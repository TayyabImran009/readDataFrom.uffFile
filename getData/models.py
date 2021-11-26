from django.db import models

# Create your models here.


class info (models.Model):
    data = models.CharField(max_length=2000)

    def __str__(self):
        return self.data
