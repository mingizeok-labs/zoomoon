from django.contrib import admin

# Register your models here.
from .models import Menu, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'display_name']
    list_filter = ['code', 'display_name']
    search_fields = ['display_name']

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['category__code', 'category__display_name', 'food']
