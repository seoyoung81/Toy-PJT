from rest_framework import serializers
from .models import Band, Album, Track, Community

# 밴드 조회        
class BandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Band
        fields = '__all__'
                
# class BanddetailSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Band
#         fields = ('name')

# 앨범 조회
class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('title', 'album_path')

class AlbumdetailSerializer(serializers.ModelSerializer):
    bands = serializers.SerializerMethodField()
    
    class Meta:
        model = Album
        fields = '__all__'
    
    def get_bands(self, album):
        bands = album.bands.all()
        return [{"name" : album.name} for band in bands]

# 밴드 & 앨범
class BandAlbumSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Album
            fields = ('title', )
