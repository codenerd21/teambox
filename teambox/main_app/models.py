from django.db import models
from django.urls import reverse

POSITIONS = (
  ('PG', 'Point Guard'),
  ('SG', 'Shooting Guard'),
  ('SF', 'Small Forward'),
  ('PF', 'Power Forward'),
  ('C', 'Center'),
)

class Team(models.Model):
  name = models.CharField(max_length=30)
  grade = models.IntegerField()
  gender = models.CharField(max_length=15)

  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'team_id': self.id})

class Player(models.Model):
  first_name = models.CharField(max_length=20)
  number = models.IntegerField()
  position = models.CharField(
    max_length=2,
    choices=POSITIONS,
    default=POSITIONS[0][0]
  )
  team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)

  def __str__(self):
    return f'{self.get_position_display()}'
  
