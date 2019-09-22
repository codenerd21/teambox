from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from itertools import chain
import boto3
import uuid
from .models import Team, Player, Strength, Photo
from .forms import PlayerForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'teambox21'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def teams_index(request):
  teams = Team.objects.all()
  return render(request, 'teams/index.html', {'teams': teams})

def teams_detail(request, team_id):
  team = Team.objects.get(id=team_id)
  player_form = PlayerForm()
  return render(request, 'teams/detail.html', 
    {'team': team, 'player_form': player_form}
  )

def add_player(request, team_id):
  form = PlayerForm(request.POST)
  if form.is_valid():
    new_player = form.save(commit=False)
    new_player.team_id = team_id
    new_player.save()
  return redirect('detail', team_id=team_id)

def add_photo(request, team_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, team_id=team_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', team_id=team_id)

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
  object_list = chain(t)
  return render(request, 'search_results.html', {'object_list': object_list})

class StrengthList(ListView):
  model = Strength





