from django.shortcuts import render
from .models import Band, Album, Track, Community
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BandSerializer, AlbumSerializer, AlbumDetailSerializer, CommunitySerializer, CommunityListSerializer, CommunityDetailSerializer
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
    serializer = AlbumDetailSerializer(albums)
    return Response(serializer.data)

@api_view(('GET',))
def community(request):
    community = Community.objects.all()
    serializer = CommunityListSerializer(community, many = True)
    return Response(serializer.data)

@api_view(('GET', 'PUT', 'DELETE'))
def community_detail(request, community_pk):
    community = Community.objects.get(pk=community_pk)
    if request.method == 'GET':
        serializer = CommunityDetailSerializer(community)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommunitySerializer(community, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data) 
    elif request.method == 'DELETE':
        community.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_community(request, band_pk):
    band = Band.objects.get(pk = band_pk)
    serializer = CommunitySerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.data(band = band)
        return Response(serializer.data)

