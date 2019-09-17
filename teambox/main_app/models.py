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

class Stat(models.Model):
  name = models.CharField(max_length=10)
  record = models.CharField(max_length=10)
  points = models.IntegerField()
  rebounds = models.IntegerField()
  assists = models.IntegerField()
  blocks = models.IntegerField()
  steals = models.IntegerField()
  threes = models.IntegerField()
  freethrows = models.IntegerField()

  def __str__(self):
    return f'{self.name} ({self.id})'

class Player(models.Model):
  first_name = models.CharField(max_length=20)
  number = models.IntegerField()
  position = models.CharField(max_length=2)

  def __str__(self):
    return f'{self.first_name} ({self.id})'
  
