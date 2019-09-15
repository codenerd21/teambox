from django.db import models
from django.core.validators import RegexValidator

class Team(models.Model):
  name = models.CharField(max_length=30)
  grade = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
  gender = models.CharField(max_length=15)

