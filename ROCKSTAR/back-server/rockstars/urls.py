from django.contrib import admin
from django.urls import path
from . import views

app_name = 'rockstars'
urlpatterns = [
    
    path('bands/', views.band_list, name="bands"),
    path('bands/<int:band_pk>/', views.band_detail, name="bands_detail"),
]
