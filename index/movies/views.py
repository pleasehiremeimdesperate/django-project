from django.shortcuts import render
from .models import Video

data = Video.objects.all()

def temp(request):
    return render(request, 'movies/video.html', {'data':data})