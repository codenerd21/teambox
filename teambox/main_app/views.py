from django.shortcuts import render

class Team():  
  def __init__(self, name, grade, gender):
    self.name = name
    self.grade = grade
    self.gender = gender

teams = [
  Team('Mid City', '6th', 'Boys'),
  Team('Willowside-1', '7th', 'Boys'),
  Team('CYO-1', '6th', 'Boys'),
  Team('CYO-2', '8th', 'Girls'),
  Team('Analy', '9th', 'Girls'),
  Team('Willowside-2', '8th', 'Girls'),
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def teams_index(request):
  return render(request, 'teams/index.html', {'teams': teams})