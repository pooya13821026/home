from django.shortcuts import render
from django.views.generic import TemplateView

from blog.models import Blog
from estate.models import Estate
from site_setting.models import *


class HomeView(TemplateView):
    template_name = 'main_page/main_page.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['special'] = Estate.objects.filter(special=True)
        context['home_baner'] = HomeBaner.objects.first()
        context['new_estate'] = Estate.objects.order_by('-create_time')[:4]
        return context


def header(request):
    settings = SiteSetting.objects.filter(main_setting=True).first()
    context = {
        'settings': settings
    }
    return render(request, 'shared/header.html', context)


def footer(request):
    footer_link_titles = FooterLinkTitle.objects.all()
    for item in footer_link_titles:
        item.footerlink_set
    settings = SiteSetting.objects.filter(main_setting=True).first()
    blog = Blog.objects.filter(is_active=True).order_by('-create_time')[:2]
    context = {
        'footer_link_titles': footer_link_titles,
        'settings': settings,
        'blog': blog
    }
    return render(request, 'shared/footer.html', context)
