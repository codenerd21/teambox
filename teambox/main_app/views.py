from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class TeamCreate(CreateView):
  model = Team
  fields = '__all__'

class TeamUpdate(UpdateView):
  model = Team
  fields = '__all__'

class TeamDelete(DeleteView):
  model = Team
  success_url = '/teams/'