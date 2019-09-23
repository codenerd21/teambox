from django.forms import ModelForm
from .models import Player, Team

class PlayerForm(ModelForm):
  class Meta:
    model = Player
    fields = ['first_name', 'number', 'position']

