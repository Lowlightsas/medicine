from django.contrib import admin
from .models import Diagnostics


@admin.register(Diagnostics)
class Diagnostics(admin.ModelAdmin):
    list_display = ['patient','date','type']
    list_filter = ['patient','date','type']
    search_fields = ('patient','date')
    ordering = ('patient','type')