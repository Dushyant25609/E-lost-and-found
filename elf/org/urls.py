from django.urls import path
from . import views


urlpatterns = [
    path('found/', views.found, name='found'),
    path('not-received/', views.not_received_items, name='not_received_items'),
    path('not-found/', views.not_found_items, name='not_found_items'),
    path('toggle_status/<int:lost_item_id>/', views.toggle_status, name='toggle_status'),
    path('search/', views.search_items, name='search_items'),
]