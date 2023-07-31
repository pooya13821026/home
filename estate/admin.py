from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['categorys']


class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ['types']


class StateAdmin(admin.ModelAdmin):
    list_display = ['state']


class WelfareAmenitiesAdmin(admin.ModelAdmin):
    list_display = ['title']


class EstateAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'special', 'is_active']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Estate, EstateAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PropertyType, PropertyTypeAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(WelfareAmenities, WelfareAmenitiesAdmin)
