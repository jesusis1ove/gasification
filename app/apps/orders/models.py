from django.db import models
# Create your models here.


class Configuration(models.Model):
    order_max_count = models.IntegerField()
    time_limit_start = models.TimeField()
    time_limit_end = models.TimeField()
