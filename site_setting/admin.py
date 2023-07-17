from django.contrib import admin

from site_setting.models import *


class SiteAdmin(admin.ModelAdmin):
    list_display = ['title', 'phone', 'email', 'main_setting']


class FooterLinkTitleAdmin(admin.ModelAdmin):
    list_display = ['title']


class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title']


class HomeBanerAdmin(admin.ModelAdmin):
    list_display = ['title', 'des']


admin.site.register(SiteSetting, SiteAdmin)
admin.site.register(FooterLink, FooterLinkAdmin)
admin.site.register(FooterLinkTitle, FooterLinkTitleAdmin)
admin.site.register(HomeBaner, HomeBanerAdmin)
