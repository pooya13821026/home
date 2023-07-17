from django.contrib import admin

from account.models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username']


admin.site.register(MyUser, MyUserAdmin)
