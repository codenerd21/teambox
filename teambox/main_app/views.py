from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from itertools import chain
from .models import Team, Player, Stat

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

class HomePageView(TemplateView):
  template_name = 'home.html'

def get_queryset(request):
  query = request.GET.get('q')
  t = Team.objects.filter(
    Q(name__icontains=query)
  )
  p = Player.objects.filter(
    Q(first_name__icontains=query)
  )
  object_list = chain(t, p)
  return render(request, 'search_results.html', {'object_list': object_list})




