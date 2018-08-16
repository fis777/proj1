from django.shortcuts import render
from django.http import HttpResponse

from .models import Genre
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def show_genres(request):
    return render(request, "genres.html", {'genres': Genre.objects.all()})
