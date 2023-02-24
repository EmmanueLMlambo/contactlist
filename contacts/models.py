from django.db import models

# Create your models here.
class Contacts(models.Model):
    full_name = models.CharField(max_length=500, blank=True)
    department = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    cell_number = models.CharField(max_length=20, blank=True)
    land_number = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name