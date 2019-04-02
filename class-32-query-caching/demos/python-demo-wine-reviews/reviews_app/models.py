from django.db import models


class Review(models.Model):
    country = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)
    designation = models.CharField(max_length=1024)
    points = models.IntegerField()
    price = models.FloatField()
    province = models.CharField(max_length=1024)
    region_1 = models.CharField(max_length=1024)
    region_2 = models.CharField(max_length=1024)
    taster_name = models.CharField(max_length=1024)
    taster_twitter_handle = models.CharField(max_length=1024)
    title = models.CharField(max_length=1024)
    variety = models.CharField(max_length=1024)
    winery = models.CharField(max_length=1024)

    def __str__(self):
        return '{}'.format(self.title)
