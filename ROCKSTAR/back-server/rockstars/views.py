from django.shortcuts import render
from .models import Band, Album, Track, Community
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BandSerializer, AlbumSerializer, AlbumdetailSerializer
from rest_framework import status

# Create your views here.

@api_view(('GET',))
def band_list(request):
    bands = Band.objects.all()
    serializer = BandSerializer(bands, many = True)
    return Response(serializer.data)

@api_view(('GET',))
def band_detail(request, band_pk):
    bands = Band.objects.get(pk = band_pk)
    serializer = BandSerializer(bands)
    return Response(serializer.data)

@api_view(('GET',))
def album_list(request):
    albums = Album.objects.all()
    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)

@api_view(('GET',))
def album_detail(request, album_pk):
    albums = Album.objects.get(pk = album_pk)
    serializer = AlbumdetailSerializer(albums)
    return Response(serializer.data)