from django.db import models
from django.urls import reverse
 
# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=100, default ='Exercise')
    musclegroups = models.CharField(max_length=100, default ='Musclegroup')
    intensity = models.IntegerField(default=0)
    directions = models.TextField(max_length=500, default='direction')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('exercise_details', kwargs={'pk': self.id})