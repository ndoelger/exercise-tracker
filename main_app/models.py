from django.db import models
from django.urls import reverse
 
# Create your models here.
class Exercise(models.Model):
    name: models.CharField(max_length=100)
    musclegroups: models.CharField(max_length=100)
    intensity: models.IntegerField()
    directions: models.TextField(max_length=500)
    completed: models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'wine_id': self.id})