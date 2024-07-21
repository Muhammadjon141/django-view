from django.contrib import admin
from .models import Shop
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Shop)
class ShopAdmin(ImportExportModelAdmin):
    list_display = ['count']
    