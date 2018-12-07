from django.shortcuts import render
from places.models import Place, Category


def home(request):
    places = Place.objects.all()
    return render(request, 'main_map.html', {'places': places})


def explore(request):
    places = Place.objects.all()
    categories = Category.objects.all()

    return render(request, 'places.html', {'places': places, 'categories': categories})


def place_info(request, id):
    place = Place.objects.get(id=id)
    similar_places = Place.objects.filter(category=place.category).exclude(id=place.id)
    return render(request, 'place.html', {'place': place, 'similar_places': similar_places})
