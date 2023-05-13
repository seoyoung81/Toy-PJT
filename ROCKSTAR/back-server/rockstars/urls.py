from django.contrib import admin
from django.urls import path
from . import views

app_name = 'rockstars'
urlpatterns = [
    
    path('bands/', views.band_list, name="bands"),
    path('bands/<int:band_pk>/', views.band_detail, name="bands_detail"),
    path('albums/', views.album_list, name="albums"),
    path('albums/<int:album_pk>/', views.album_detail, name="albums_detail"),
    # path('community/', views.community, name="community"),
    # path('community/<int:community_pk>/', views.community_detail, name="community_detail"),
    # path('bands/<int:band_pk>/create_community', views.create_community, name="create_community"),
    
]
