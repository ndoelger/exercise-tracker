from django.db import models
from django.urls import reverse
 
# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    musclegroups = models.CharField('Muscle Groups', max_length=100)
    intensity = models.IntegerField()
    directions = models.TextField(max_length=500,)
    # completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('exercise_details', kwargs={'exercise_id': self.id})
    
class Completion(models.Model):
    date = models.DateField('Exercise Date')
    reps = models.IntegerField()
    sets = models.IntegerField()
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.date}, {self.reps}, {self.sets}, {self.exercise}"
    
    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for exercise: {self.exercise} @{self.url}"