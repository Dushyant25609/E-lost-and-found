from django.urls import path
from . import views


urlpatterns = [
    path('found/', views.found, name='found'),
    path('not-received/', views.not_received_items, name='not_received_items'),
    path('not-found/', views.not_found_items, name='not_found_items'),
]