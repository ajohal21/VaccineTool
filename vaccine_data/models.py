from django.db import models

# Create your models here.

class Vaccine(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Country(models.Model):
    name = models.CharField(max_length=100)
    vaccines = models.ManyToManyField(Vaccine, related_name='countries')
    
    def __str__(self):
        return self.name


