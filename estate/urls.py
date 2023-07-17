from django.urls import path
from . import views

urlpatterns = [
    path('', views.EstateListView.as_view(), name='estate_list'),
    path('<str:slug>', views.EstateDeteilView.as_view(), name='estate_deteil'),
    path('property-type/<pro>', views.EstateListView.as_view(), name='property_type'),
    path('category/<cat>', views.EstateListView.as_view(), name='category'),
    path('search/', views.search, name='search'),
]
