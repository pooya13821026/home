from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView

from contact_us.forms import ContactUsForm
from contact_us.models import ContactUs
from site_setting.models import SiteSetting


class ContactUsView(CreateView):
    template_name = 'contact_us/contact_us.html'
    form_class = ContactUsForm
    success_url = '/contact-us/'

    def get_context_data(self, **kwargs):
        context = super(ContactUsView, self).get_context_data()
        context['site'] = SiteSetting.objects.filter(main_setting=True).first()
        return context

