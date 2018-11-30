from django.shortcuts import render
from places.models import Place


def home(request):
    return render(request, 'main_map.html', {})


def explore(request):
    places = Place.objects.all()
    categories = [x[1] for x in Place.CATEGORY_CHOICES]

    return render(request, 'places.html', {'places': places, 'categories': categories})
