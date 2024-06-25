from django.shortcuts import render
from .models import New_film
from .forms import New_FilmForm

# Create your views here.
def index(request):
    return render(request, 'films/index.html')

def movies(request):
    films = New_film.objects.all()
    return render(request, 'films/movies.html', {'films': films})

def create_films(request):
    form = New_FilmForm()
    return render(request, 'films/add_new_films.html', {'form':form})