from django.urls import path
from . import views

urlpatterns = [
  path('', views.HomePageView.as_view(), name='home'),
  path('search/', views.get_queryset, name='search_results'),
  path('about/', views.about, name='about'),
  path('teams/', views.teams_index, name='index'),
  path('teams/<int:team_id>/', views.teams_detail, name='detail'),
  path('teams/create/', views.TeamCreate.as_view(), name='team_create'),
  path('teams/<int:pk>/update/', views.TeamUpdate.as_view(), name='team_update'),
  path('teams/<int:pk>/delete/', views.TeamDelete.as_view(), name='team_delete'),
  path('teams/<int:team_id>/add_player/', views.add_player, name='add_player'),
]

