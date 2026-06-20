from django.contrib import admin
from .models import Workers, OnVacation, DataAnalyze
# Register your models here.

@admin.register(Workers)
class WorkersAdm(admin.ModelAdmin):
    fields = ['name', 'surname', 'data_checked_per_day']
    search_fields = ('name', 'surname')
    list_display = ('name', 'surname')

@admin.register(OnVacation)
class OnVacAdm(admin.ModelAdmin):
    fields = ['name', 'surname']
    search_fields = ('name', 'surname')
    list_display = ('name', 'surname')

@admin.register(DataAnalyze)
class DataAnalyzeAdm(admin.ModelAdmin):
    fields = ['data', 'description', 'type']
    search_fields = ('data', 'type')
    list_display = ('data', 'type')