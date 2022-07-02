from rest_framework import serializers, status
from groups.serializers import GroupSerializer
from characteristics.serializers import CharacteristicSerializer
from animals.models import Animal
from characteristics.models import Characteristic

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    
    name = serializers.CharField(required=True)
    age = serializers.FloatField(required=True)
    weight = serializers.FloatField(required=True)
    sex = serializers.CharField(required=True)
    
    group = GroupSerializer(read_only=True)
    characteristic = CharacteristicSerializer(read_only=True)
    
    def create(self, validated_data):
        group = validated_data.pop('group')
        characteristics = validated_data.pop('characteristic')
        
        animal = Animal.objects.create(**validated_data, group=group)
        
        for characteristic in characteristics:
            characteristic, _ = Characteristic.objects.get_or_create(**characteristic)
            animal.characteristic.add(characteristic)
            
        return animal
    
    def update(self, instance, validated_data):
        not_updatable_fields = ['sex', 'group']
        
        for key, value in validated_data.items():
            if key in not_updatable_fields:
                raise KeyError({ "message": f"You can not update '{key}' property."}, status.HTTP_422_UNPROCESSABLE_ENTITY)
                setattr(instance, key, value)
                instance.save()
            
        return instance