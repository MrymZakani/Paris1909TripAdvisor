from django.contrib import admin

# Register your models here.
from places.models import Neighborhood, MetroStation, Place, PlaceImage, Menu, MenuOption


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage


@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(MetroStation)
class MetroStationAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'address',
        'coordinate_x', 'coordinate_y', 'map_id', 'type',)
    inlines = [PlaceImageInline, ]

@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'link', 'type')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'place')


@admin.register(MenuOption)
class MenuOptionItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'menu')
