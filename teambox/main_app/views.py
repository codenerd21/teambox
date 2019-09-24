from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from itertools import chain
import boto3
import uuid
from .models import Team, Player, Strength, Photo
from .forms import PlayerForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'teambox21'

class TeamCreate(CreateView):
  model = Team
  fields = ['name', 'grade', 'gender']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def teams_index(request):
  teams = Team.objects.filter(user=request.user)
  return render(request, 'teams/index.html', {'teams': teams})

@login_required
def teams_detail(request, team_id):
  team = Team.objects.get(id=team_id)
  avail_strengths = Strength.objects.exclude(id__in = team.strengths.all().values_list('id'))
  player_form = PlayerForm()
  return render(request, 'teams/detail.html', 
    {
      'team': team, 
      'player_form': player_form,
      'avail_strengths': avail_strengths
    }
  )

@login_required
def add_player(request, team_id):
  form = PlayerForm(request.POST)
  if form.is_valid():
    new_player = form.save(commit=False)
    new_player.team_id = team_id
    new_player.save()
  return redirect('detail', team_id=team_id)

@login_required
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

class TeamUpdate(LoginRequiredMixin, UpdateView):
  model = Team
  fields = '__all__'

class TeamDelete(LoginRequiredMixin, DeleteView):
  model = Team
  success_url = '/teams/'

class HomePageView(TemplateView):
  template_name = 'home.html'

@login_required
def get_queryset(request):
  query = request.GET.get('q')
  t = Team.objects.filter(
    Q(name__icontains=query)
  )
  object_list = chain(t)
  return render(request, 'search_results.html', {'object_list': object_list})

class StrengthList(LoginRequiredMixin, ListView):
  model = Strength

class StrengthDetail(LoginRequiredMixin, DetailView):
  model = Strength

class StrengthCreate(LoginRequiredMixin, CreateView):
  model = Strength
  fields = '__all__'

class StrengthUpdate(LoginRequiredMixin, UpdateView):
  model = Strength
  fields = '__all__'

class StrengthDelete(LoginRequiredMixin, DeleteView):
  model = Strength
  success_url = '/strength/'

@login_required
def assoc_strength(request, team_id, strength_id):
  Team.objects.get(id=team_id).strengths.add(strength_id)
  return redirect('detail', team_id=team_id)

@login_required
def unassoc_strength(request, team_id, strength_id):
  Team.objects.get(id=team_id).strengths.remove(strength_id)
  return redirect('detail', team_id=team_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

