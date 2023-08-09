from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from estate.forms import SearchForm, EstateForm
from estate.models import *


class EstateListView(ListView):
    model = Estate
    template_name = 'estate/estate_list.html'

    def get_queryset(self):
        query = super(EstateListView, self).get_queryset()
        deta = query.filter(is_active=True)
        category = self.kwargs.get('cat')
        if category is not None:
            deta = query.filter(category__url_title__iexact=category)
            return deta
        property_types = self.kwargs.get('pro')
        if property_types is not None:
            deta = query.filter(property_type__url_title__iexact=property_types)
            return deta
        return deta


def estate_categris(request):
    estate_categris = Category.objects.all()
    context = {
        'estate_categris': estate_categris,
    }
    return render(request, 'estate/component/category.html', context)


def property_types(request):
    property_typess = PropertyType.objects.all()
    context = {
        'property_types': property_typess,
    }
    return render(request, 'estate/component/property_types.html', context)


class EstateDeteilView(DetailView):
    model = Estate
    template_name = 'estate/estate_deteil.html'
    context_object_name = 'estates'


def search(request):
    estate = Estate.objects.filter(is_active=True)
    form = SearchForm()
    if 'search' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data['search']
            estate = estate.filter(title__icontains=cd)
    return render(request, 'estate/estate_list.html', {'form': form, 'estate_list': estate})


class CreateEstate(View):
    def get(self, request: HttpRequest):
        property_type = PropertyType.objects.all()
        category = Category.objects.all()
        state = State.objects.all()
        welfare_amenities = WelfareAmenities.objects.all()
        context = {
            'property_type': property_type,
            'category': category,
            'state': state,
            'welfare_amenities': welfare_amenities,
        }
        return render(request, 'estate/create_estate.html', context)

    def post(self, request: HttpRequest):
        if request.method == 'POST':
            print(request.POST)
            form = EstateForm(request.POST)
            print(form.data)
            if form.is_valid():
                print(form.data)
            else:
                print(form.errors.as_data())
                print(form.errors)
                print('form is not valid')
        property_type = PropertyType.objects.all()
        category = Category.objects.all()
        state = State.objects.all()
        welfare_amenities = WelfareAmenities.objects.all()
        context = {
            'property_type': property_type,
            'category': category,
            'state': state,
            'welfare_amenities': welfare_amenities,
        }
        return render(request, 'estate/create_estate.html', context)
