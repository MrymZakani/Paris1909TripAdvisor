from django.db import models


class Neighborhood(models.Model):
    name = models.TextField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class MetroStation(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    image = models.URLField()

    def __str__(self):
        return self.name


class Place(models.Model):
    BALL = 'ba'
    CONCERT = 'co'
    MUSIC_HALL = 'mh'
    CIRQUE = 'ci'
    RESTAURANT = 're'
    RESTAURANT_DE = 'rn'
    THEATRE = 'th'
    CABARET = 'ca'
    PATINAGE = 'pa'
    OTHER = 'ot'

    CATEGORY_CHOICES = (
        (BALL, 'Ball'),
        (CONCERT, 'Cafe/Concert'),
        (MUSIC_HALL, 'Music hall'),
        (CIRQUE, 'Cirque'),
        (RESTAURANT, 'Restaurant'),
        (RESTAURANT_DE, 'Restaurant de nuit'),
        (THEATRE, 'Theatre'),
        (CABARET, 'Cabaret'),
        (PATINAGE, 'Skating'),
        (OTHER, 'Other'),
    )

    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    description_orig = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    coordinate_x = models.IntegerField(null=True, blank=True)
    coordinate_y = models.IntegerField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    map_id = models.IntegerField()
    type = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    nearest_metro = models.ForeignKey(MetroStation, on_delete=models.CASCADE, null=True, blank=True)
    geo_name_id = models.TextField(null=True, blank=True)
    wiki_data_link = models.URLField(null=True, blank=True)
    phone_number = models.TextField(null=True, blank=True, max_length=50)

    def get_first_image(self):
        if len(self.images.all()) > 0:
            return self.images.all()[0].link
        return "https://www.freeiconspng.com/uploads/no-image-icon-4.png"

    def get_x(self):
        return int(
            self.coordinate_x * 100 / 4000) if self.coordinate_x and self.coordinate_x < 4000 and self.coordinate_x > 0 else None

    def get_y(self):
        return int(
            self.coordinate_y * 100 / 2684) if self.coordinate_y and self.coordinate_y < 2684 and self.coordinate_y > 0 else None

    def __str__(self):
        return self.name


class PlaceImage(models.Model):
    POSTER = 'po'
    PHOTO = 'ph'
    HAND_MADE = 'hm'

    TYPE_CHOICES = (
        (POSTER, 'Poster'),
        (PHOTO, 'Photo'),
        (HAND_MADE, 'Hand made'),
    )
    link = models.URLField()
    desc = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    is_black_white = models.BooleanField(default=False)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return str(self.id) + "/" + str(self.place.name) + "---" + str(self.type)


class Menu(models.Model):
    name = models.TextField(null=True, blank=True)
    hour_from = models.TimeField(null=True, blank=True)
    hour_to = models.TimeField(null=True, blank=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.place.name) + "--" + str(self.name)


class MenuOption(models.Model):
    name = models.TextField()
    cost = models.FloatField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.menu) + "--" + str(self.name)


class Schedule(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE)
    only_night = models.BooleanField(default=False)

    def __str__(self):
        return str(self.place) + " Schedule"


class DaySchedule(models.Model):
    MONDAY = 'mo'
    TUESDAY = 'tu'
    WEDNESDAY = 'we'
    THURSDAY = 'th'
    FRIDAY = 'fr'
    SATURDAY = 'sa'
    SUNDAY = 'so'
    HOLIDAY = 'ho'
    ALL_WEEK = 'al'

    DAY_CHOICES = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
        (HOLIDAY, 'Holiday'),
        (ALL_WEEK, 'All days of week'),
    )

    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=DAY_CHOICES)
    opens_at = models.TimeField(null=True, blank=True)
    closes_at = models.TimeField(null=True, blank=True)

    def __str__(self):
        return str(self.schedule) + "--" + str(self.type)


class Cost(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE)

    def __str__(self):
        return "Cost of " + str(self.place.name)


class BallCost(Cost):
    entrance_from = models.FloatField(null=True, blank=True)
    entrance_to = models.FloatField(null=True, blank=True)
    woman_from = models.FloatField(null=True, blank=True)
    woman_to = models.FloatField(null=True, blank=True)
    man_from = models.FloatField(null=True, blank=True)
    man_to = models.FloatField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)


class CabaretCost(Cost):
    entrance_from = models.FloatField(null=True, blank=True)
    entrance_to = models.FloatField(null=True, blank=True)
    glass_from = models.FloatField(null=True, blank=True)
    glass_to = models.FloatField(null=True, blank=True)


class PatinageCost(Cost):
    cost_from = models.FloatField(null=True, blank=True)
    cost_to = models.FloatField(null=True, blank=True)


class AuditoriumTypeCost(models.Model):
    BALCONIES = 'ba'
    GALLERIES = 'ga'
    BOXES = 'bo'
    STALLES = 'st'
    BAIGNOIRES = 'bg'
    STANDING_ROOMS = 'sr'
    DRESS_CIRCLE = 'dc'
    AVANT_SCENE = 'as'

    TYPE_CHOICES = (
        (BALCONIES, 'Balconies'),
        (GALLERIES, 'Galleries'),
        (BOXES, 'Boxes'),
        (STALLES, 'Stalles'),
        (BAIGNOIRES, 'Baignoires'),
        (STANDING_ROOMS, 'Standing rooms'),
        (DRESS_CIRCLE, 'Dress circles'),
        (AVANT_SCENE, 'Avant Scenes'),
    )
    cost = models.ForeignKey(Cost, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    cost_from = models.FloatField(null=True, blank=True)
    cost_to = models.FloatField(null=True, blank=True)
