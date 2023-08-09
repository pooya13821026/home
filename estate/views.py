from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from estate.forms import SearchForm, EstateForm
from estate.models import *

def estate_list_view(request):
    qs = Estate.objects.all().filter(is_active=True)
    category = request.GET.get('category')  
    if category:
        qs = qs.filter(category__url_title__iexact=category)
    if request.method == "POST":
        print(request.POST)
        state = request.POST.get('state')
        if state:
            qs = qs.filter(state__state=state)
        
        property_type = request.POST.get('property_type')
        print(property_type) 
        if property_type:
            qs = qs.filter(property_type__types=property_type)
        
        min_meterage = request.POST.get('min-meterage') or None
        max_meterage = request.POST.get('max-meterage') or None
        if min_meterage:
            qs = qs.filter(meterage__gte=min_meterage)
        if max_meterage:
            qs = qs.filter(meterage__lte=max_meterage)
    context = {
        'estates' : qs,
    }
    return render(request, 'estate/estate_list_copy.html', context)  

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
    def get(self, request):
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

    def post(self, request):
        if request.method == 'POST':
            form = EstateForm(request.POST)
            print(form)
            if form.is_valid():
                print(form)
            else:
                print(form.errors.as_data())
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
