from rest_framework import serializers
from .models import Band, Album, Track, Community

# 밴드 조회        
class BandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Band
        fields = '__all__'
                
# 앨범 조회
class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('title', 'album_path')

class AlbumDetailSerializer(serializers.ModelSerializer):
    band = BandSerializer(read_only=True, source="bands")
    
    class Meta:
        model = Album
        # fields = '__all__'
        exclude = ('bands',)
   
    
# 밴드 & 앨범
class BandAlbumSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Album
            fields = ('title', )


# 커뮤니티
class CommunitySerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Community
        fields = '__all__'

        read_only_fields = ('band', )    

class CommunityListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Community
        fields = '__all__'

class CommunityDetailSerializer(serializers.ModelSerializer):
    band = BandSerializer(read_only=True, source="bands")


    class Meta:
        model = Community
        fields = '__all__'
