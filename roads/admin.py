from django.contrib import admin
from .models import Road, LandPlot


@admin.register(Road)
class RoadsAdmin(admin.ModelAdmin):
    list_display = ('ident_number', 'name', 'kad_number')


@admin.register(LandPlot)
class LandPlotAdmin(admin.ModelAdmin):
    list_display = ('kad_number', 'status', 'square', 'road')
    list_filter = ('road',)
