from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lost/', views.lost, name='lost'),
    path('found/', views.found, name='found'),
    path('user/requested-items/', views.user_requested_items, name='user_requested_items'),
    path('about/', views.about, name='about'),
]