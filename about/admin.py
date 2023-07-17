from django.contrib import admin
from about.models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = ['title1', 'main']


admin.site.register(About, AboutAdmin)
