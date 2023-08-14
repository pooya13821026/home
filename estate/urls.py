from django.urls import path
from .views import (
    EstateListView,
    EstateDetailView,
    CreateEstate
)

urlpatterns = [
    path('<category>', EstateListView.as_view(), name='category'),
    path('', EstateListView.as_view(), name='estate_list'),
    path('detail/<int:pk>', EstateDetailView.as_view(), name='estate_detail'),
    # path('property-type/<pro>', views.EstateListView.as_view(), name='property_type'),
    # path('search/', views.search, name='search'),
    path('create-estate/', CreateEstate.as_view(), name='create_estate'),
]
