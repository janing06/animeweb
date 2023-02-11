from django.shortcuts import render
from .models import Characters

def home(request):
    

    return render(request, 'demonslayer/home.html')

def character(request):
    
    characters = Characters.objects.all()

    context = {
        'characters': characters,
    }

    return render(request, 'demonslayer/character.html',context)

def videos(request):
    

    return render(request, 'demonslayer/videos.html')