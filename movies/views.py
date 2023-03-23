from django.shortcuts import render
from .models import *
from user.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def movies(request, slug, pk):
    filmler = Movie.objects.all()
    profiller = Profile.objects.filter(owner = request.user)
    profil = Profile.objects.filter(slug = slug).get(id = pk)
    context = {
        'filmler':filmler,
        'profil':profil,
        'profiller':profiller
    }
    return render(request, 'browse-index.html', context)