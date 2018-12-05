from django.shortcuts import render
from places.models import Place, Category


def home(request):
    return render(request, 'main_map.html', {})


def explore(request):
    places = Place.objects.all()
    categories = Category.objects.all()

    return render(request, 'places.html', {'places': places, 'categories': categories})
