from django.db import models


class DataSet(models.Model):
    area = models.CharField(max_length=100)
    gps_cordinates = models.CharField(max_length=100)
    demographic_data = models.CharField(max_length=100)
    satellite_images = models.CharField(max_length=500)
    news_articles = models.TextField()
    geo_data = models.CharField(max_length=1000)

    def __str__(self):
        return self.area
