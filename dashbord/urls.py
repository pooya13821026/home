from django.urls import path

from dashbord import views

urlpatterns = [
    path('', views.Dashbord.as_view(), name='dashbord'),
    path('edit-profile/', views.EditProfile.as_view(), name='edit_profile'),
    path('change-pass/', views.ChangePass.as_view(), name='change_pass'),
    path('new-home/', views.NewHome.as_view(), name='new_home'),
]
