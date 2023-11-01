from django.db import models
# import reverse function 
from django.urls import reverse
# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length = 100)
    breed = models.CharField(max_length = 100)
    description = models.TextField(max_length = 1000)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.breed})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs = {
            'finch_id': self.id
        })