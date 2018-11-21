from django.db import models


class Neighborhood(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class MetroStation(models.Model):
    name = models.TextField()

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
    )

    name = models.TextField()
    description = models.TextField()
    description_orig = models.TextField()
    address = models.TextField()
    coordinate_x = models.IntegerField()
    coordinate_y = models.IntegerField()
    map_id = models.IntegerField()
    type = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    comment = models.TextField()
    nearest_metro = models.ForeignKey(MetroStation, on_delete=models.CASCADE)

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
    desc = models.TextField()
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    is_black_white = models.BooleanField(default=False)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + "/" + str(self.place.name) + "---" + str(self.type)


class Menu(models.Model):
    name = models.TextField()
    # hour = models.TextField() TODO
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return str(self.place.name) + "--" + str(self.name)


class MenuOption(models.Model):
    name = models.TextField()
    cost = models.FloatField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.menu) + "--" + str(self.name)
