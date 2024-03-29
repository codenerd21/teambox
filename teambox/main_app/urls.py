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
  path('teams/<int:team_id>/add_photo/', views.add_photo, name='add_photo'),
  path('teams/<int:team_id>/assoc_strength/<int:strength_id>/', views.assoc_strength, name='assoc_strength'),
  path('teams/<int:team_id>/unassoc_strength/<int:strength_id>/', views.unassoc_strength, name='unassoc_strength'),
  path('strength/', views.StrengthList.as_view(), name='strength_index'),
  path('strength/<int:pk>/', views.StrengthDetail.as_view(), name='strength_detail'),
  path('strength/create/', views.StrengthCreate.as_view(), name='strength_create'),
  path('strength/<int:pk>/update/', views.StrengthUpdate.as_view(), name='strength_update'),
  path('strength/<int:pk>/delete/', views.StrengthDelete.as_view(), name='strength_delete'),
  path('accounts/signup', views.signup, name='signup'),
]

