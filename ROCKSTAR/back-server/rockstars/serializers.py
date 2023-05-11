from rest_framework import serializers
from .models import Band, Album, Track, Community

# 밴드 조회        
class BandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Band
        fields = '__all__'
                
