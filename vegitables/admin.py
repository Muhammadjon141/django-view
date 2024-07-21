from django.contrib import admin
from .models import Vegitable, Type, Mavsum, Fruit
from import_export.admin import ImportExportModelAdmin

@admin.register(Type)
class TypeAdmin(ImportExportModelAdmin):
    list_display = ['types']

@admin.register(Mavsum)
class MavsumAdmin(ImportExportModelAdmin):
    list_display = ['mavsum']

@admin.register(Vegitable)
class VegitableAdmin(ImportExportModelAdmin):
    list_display = ['name', 'price']
    list_display_links = ['name', 'price']
    
@admin.register(Fruit)
class FruitAdmin(ImportExportModelAdmin):
    list_display = ['name', 'price']
    list_display_links = ['name', 'price']