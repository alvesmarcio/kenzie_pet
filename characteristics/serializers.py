from rest_framework import serializers, status
from .models import Characteristic

class CharacteristicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    
    name = serializers.CharField(required=True)
    
    def create(self, validated_data):
        characteristic, created = Characteristic.objects.get_or_create(**validated_data)
        
        if not created:
            raise ValueError(
                {"message": f"`{validated_data['name']}` already exists."}, status.HTTP_409_CONFLICT
            )
        
        return characteristic