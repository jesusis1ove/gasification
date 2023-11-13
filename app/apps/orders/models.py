from django.db import models
from django.contrib.auth import get_user_model

from ..erp_data.models import ConstructionObject, Counterparty


class Configuration(models.Model):
    order_max_count = models.IntegerField()
    time_limit_start = models.TimeField()
    time_limit_end = models.TimeField()


ORDER_STATUSES = (
    ('created', 'создана'),
    ('accepted', 'принята'),
    ('canceled', 'отменена'),
)


class Order(models.Model):
    counterparty_guid = models.CharField(max_length=36)
    construction_object_guid = models.CharField(max_length=36)
    applicant = models.CharField(max_length=250)
    date = models.DateField()
    status = models.CharField(choices=ORDER_STATUSES, max_length=100)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



