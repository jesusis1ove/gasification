from django.contrib import admin

from .models import Configuration, Order


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'counterparty_guid', 'created_by')
