from django.db import models
# import reverse function 
from django.urls import reverse
# import date function
from datetime import date
# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

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
    
    def fed_for_today(self):
        return self.feeding_set.filter(date = date.today()).count() >= len(MEALS)
    
class Feeding(models.Model):
    date = models.DateField('feeding Date')
    meal = models.CharField(
        max_length = 1,
        choices = MEALS,
        default = MEALS[0][0],
    )
    # finch_id foreign key
    finch = models.ForeignKey(
        Finch,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']