from django.contrib import admin

from .models import Counterparties


@admin.register(Counterparties)
class CounterpartiesAdmin(admin.ModelAdmin):
    pass