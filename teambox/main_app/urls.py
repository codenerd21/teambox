from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('teams/', views.teams_index, name='index'),
  path('teams/<int:team_id>/', views.teams_detail, name='detail'),
  path('teams/create/', views.TeamCreate.as_view(), name='team_create'),
]

