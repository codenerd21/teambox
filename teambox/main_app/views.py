from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Home Page - Returning HTTP Response</h1>')

def about(request):
  return HttpResponse('<h1>About the Team Box</h1>')

#Code below from Tasty


# def home(request):
#     return render(
#         request,
#         'main/home.html',
#     )
