from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog_list'),
    path('<str:slug>', views.BlogDeteilView.as_view(), name='blog_deteil'),
    path('send-comment', views.send_comment, name='send_comment'),
]
