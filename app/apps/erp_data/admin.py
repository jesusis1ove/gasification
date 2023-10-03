from django.contrib import admin

from .models import Counterparty, ConstructionObject, OrderType


@admin.register(Counterparty)
class CounterpartyAdmin(admin.ModelAdmin):
    pass


@admin.register(ConstructionObject)
class ConstructionObjectAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderType)
class OrderTypeAdmin(admin.ModelAdmin):
    pass