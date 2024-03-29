from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


POSITIONS = (
  ('PG', 'Point Guard'),
  ('SG', 'Shooting Guard'),
  ('SF', 'Small Forward'),
  ('PF', 'Power Forward'),
  ('C', 'Center'),
)

class Strength(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('strength_detail', kwargs={'pk': self.id})

class Team(models.Model):
  name = models.CharField(max_length=30)
  grade = models.IntegerField()
  gender = models.CharField(max_length=15)
  strengths = models.ManyToManyField(Strength)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'team_id': self.id})

class Player(models.Model):
  first_name = models.CharField(max_length=20)
  number = models.IntegerField(default=0)
  position = models.CharField(
    max_length=2,
    choices=POSITIONS,
    default=POSITIONS[0][0]
  )
  team = models.ForeignKey(Team, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.first_name}'

  class Meta:
    ordering = ['first_name']
  
class Photo(models.Model):
  url = models.CharField(max_length=200)
  team = models.ForeignKey(Team, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for team_id: {self.team_id} @{self.url}"
  