from django.shortcuts import render
from django.views.generic import TemplateView

from about.models import About


class AboutView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data()
        context['about'] = About.objects.filter(main=True)
        return context

