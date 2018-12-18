from django.shortcuts import render
from places.models import Place, Category, District, Experience


def home(request):
    places = Place.objects.all()
    return render(request, 'main_map.html', {'places': places})


def explore(request):
    places = Place.objects.all()
    categories = Category.objects.all()
    districts = District.objects.all().order_by('order')
    experiences = Experience.objects.all().order_by('order')
    return render(request, 'places.html', {'places': places,
                                           'categories': categories,
                                           'districts': districts,
                                           'experiences': experiences})


def explore_category(request, id):
    category = Category.objects.get(id=id)
    places = Place.objects.filter(category=category)
    categories = Category.objects.all()
    districts = District.objects.all().order_by('order')
    experiences = Experience.objects.all().order_by('order')
    return render(request, 'places.html', {'places': places,
                                           'category_id': category.id,
                                           'categories': categories,
                                           'districts': districts,
                                           'experiences': experiences})


def find(request):
    places = Place.objects.all()

    search_for = request.GET.get('search_for')
    print(search_for)
    if search_for:
        places = places.filter(name__icontains=search_for)

    return render(request, 'find_places.html', {'places': places})


def place_info(request, id):
    place = Place.objects.get(id=id)
    similar_places = Place.objects.filter(category=place.category).exclude(id=place.id)
    return render(request, 'place.html', {'place': place, 'similar_places': similar_places})
