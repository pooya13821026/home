from django import template
from jalali_date import date2jalali

register = template.Library()


@register.filter(name='persian_deta')
def get_persian_date(value):
    return date2jalali(value).strftime('%Y/%m/%d')
