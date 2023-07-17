from django.contrib import admin

from contact_us.models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'mobile', 'is_read']


admin.site.register(ContactUs, ContactUsAdmin)
