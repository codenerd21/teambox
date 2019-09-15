from django.db import models
from django.urls import reverse

class Team(models.Model):
  name = models.CharField(max_length=30)
  grade = models.IntegerField()
  gender = models.CharField(max_length=15)

  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'team_id': self.id})

