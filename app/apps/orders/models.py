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
    ('cancelled', 'отменена'),
    ('on_confirm', 'на согласовании')
)


class Order(models.Model):
    counterparty_guid = models.CharField(max_length=36)
    construction_object_guid = models.CharField(max_length=36)
    applicant = models.CharField(max_length=250)
    date = models.DateField()
    date_confirm = models.DateField(blank=True, null=True)
    status = models.CharField(choices=ORDER_STATUSES, max_length=100, default='created')
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def set_accepted(self):
        if self.status in ('created', 'on_confirm'):
            self.status = 'accepted'
            self.save()

    def set_cancelled(self):
        if self.status in ('created', 'accepted',):
            self.status = 'cancelled'
            self.save()

    def set_on_confirm(self, date_confirm):
        if self.status in ('created',):
            self.status = 'on_confirm'
            self.date_confirm = date_confirm
            self.save()





