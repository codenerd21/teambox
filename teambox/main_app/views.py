from django.shortcuts import render
from .models import Team

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def teams_index(request):
  teams = Team.objects.all()
  return render(request, 'teams/index.html', {'teams': teams})

def teams_detail(request, team_id):
  team = Team.objects.get(id=team_id)
  return render(request, 'teams/detail.html', {'team': team})
