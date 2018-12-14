from django.contrib import admin

# Register your models here.
from places.models import Neighborhood, MetroStation, Place, PlaceImage, Menu, MenuOption, Schedule, DaySchedule, Cost, \
    BallCost, CabaretCost, PatinageCost, AuditoriumTypeCost, Category, Experience, ExperiencePlace, District, \
    DistrictPlace


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage


class MenuOptionInline(admin.TabularInline):
    model = MenuOption


class ScheduleInline(admin.TabularInline):
    model = Schedule


class DayScheduleInline(admin.TabularInline):
    model = DaySchedule


class AuditoriumTypeCostInline(admin.TabularInline):
    model = AuditoriumTypeCost


@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
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
    inlines = [MenuOptionInline, ]


@admin.register(MenuOption)
class MenuOptionItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'menu')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('place',)
    inlines = [DayScheduleInline, ]


@admin.register(DaySchedule)
class DayScheduleAdmin(admin.ModelAdmin):
    list_display = ('schedule', 'type', 'opens_at', 'closes_at')


@admin.register(BallCost)
class BallCostAdmin(admin.ModelAdmin):
    list_display = ('place',)


@admin.register(CabaretCost)
class CabaretCostAdmin(admin.ModelAdmin):
    list_display = ('place',)


@admin.register(PatinageCost)
class PatinageCostAdmin(admin.ModelAdmin):
    list_display = ('place',)


@admin.register(AuditoriumTypeCost)
class AuditoriumTypeCostAdmin(admin.ModelAdmin):
    list_display = ('cost', 'cost_from', 'cost_to')


@admin.register(Cost)
class AuditoriumCostAdmin(admin.ModelAdmin):
    list_display = ('place',)
    inlines = [AuditoriumTypeCostInline, ]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')


@admin.register(ExperiencePlace)
class ExperiencePlaceAdmin(admin.ModelAdmin):
    list_display = ('experience', 'place')


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


@admin.register(DistrictPlace)
class DistrictPlaceAdmin(admin.ModelAdmin):
    list_display = ('district', 'place')
