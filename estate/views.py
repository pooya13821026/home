from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from estate.forms import SearchForm, EstateForm
from estate.models import *


class EstateListView(ListView):
    context_object_name = "estate_list"
    template_name = 'estate/estate_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Estate.objects.filter(is_active=True)
        request = self.request.GET
        category = self.kwargs.get('category', 'real-estate')
        if category != 'real-estate':
            queryset = queryset.filter(category__url_title__iexact=category)

        search = request.get('search') or None
        if search is not None:
            queryset = queryset.filter(title__icontains=search)

        state = request.get('state') or None
        if state:
            queryset = queryset.filter(state__state=state)

        property_type = request.get('property_type') or None
        if property_type:
            queryset = queryset.filter(property_type__types=property_type)

        min_price = request.get('min-price') or None
        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        max_price = request.get('max-price') or None
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        min_meterage = request.get('min-meterage') or None
        if min_meterage:
            queryset = queryset.filter(meterage__gte=min_meterage)

        max_meterage = request.get('max-meterage') or None
        if max_meterage:
            queryset = queryset.filter(meterage__lte=max_meterage)

        bedrooms = request.get('bedrooms')
        if bedrooms:
            if bedrooms == '4':
                queryset = queryset.filter(room__gte=int(bedrooms))
            else:
                queryset = queryset.filter(room=int(bedrooms))

        bathrooms = request.get('bathrooms')
        if bathrooms:
            if bathrooms == '4':
                queryset = queryset.filter(wc__gte=int(bathrooms))
            else:
                queryset = queryset.filter(wc=int(bathrooms))

        return queryset


def estate_categorys(request):
    estate_categorys = Category.objects.all()
    context = {
        'estate_categorys': estate_categorys,
    }
    return render(request, 'estate/component/category.html', context)


def property_types(request):
    property_types = PropertyType.objects.all()
    context = {
        'property_types': property_types,
    }
    return render(request, 'estate/component/property_types.html', context)


def states(request):
    states = State.objects.all()
    context = {
        'states': states,
    }
    return render(request, 'estate/component/states.html', context)


def other_facilities(request):
    facilities = WelfareAmenities.objects.all()
    context = {
        'facilities': facilities,
    }
    return render(request, 'estate/component/other_facilities.html', context)


class EstateDetailView(DetailView):
    model = Estate
    template_name = 'estate/estate_detail.html'
    context_object_name = 'estates'


# def search(request):
#     estate_list = Estate.objects.filter(is_active=True)
#     form = SearchForm()
#     if 'search' in request.GET:
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             search = form.cleaned_data['search']
#             estate_list = estate_list.filter(title__icontains=search)
#             print(search, estate_list)
#     return render(request, 'estate/estate_list.html', {'form': form, 'estate_list': estate_list})


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
