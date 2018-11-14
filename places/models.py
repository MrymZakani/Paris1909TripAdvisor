from django.db import models


class Place(models.Model):
    BAR = 'b'
    RESTAURANT = 'r'
    THEATRE = 't'
    CATEGORY_CHOICES = (
        (BAR, 'Bar'),
        (RESTAURANT, 'Restaurant'),
        (THEATRE, 'Theatre'),
    )

    name = models.TextField()
    description = models.TextField()
    address = models.TextField()
    coordinate_x = models.IntegerField()
    coordinate_y = models.IntegerField()
    map_id = models.IntegerField()
    type = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    # specific_type =
    # neighborhood =
    # cost
    # working hour
    photo = models.URLField()  # TODO: how many
    poster = models.URLField()  # TODO: how many
