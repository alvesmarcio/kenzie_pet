from rest_framework import serializers, status
from groups.serializers import GroupSerializer
from characteristics.serializers import CharacteristicSerializer
from animals.models import Animal
from characteristics.models import Characteristic
from groups.models import Group

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    
    name = serializers.CharField(required=True)
    age = serializers.FloatField(required=True)
    weight = serializers.FloatField(required=True)
    sex = serializers.CharField(required=True)
    
    group = GroupSerializer()
    characteristics = CharacteristicSerializer(many=True)
    
    def create(self, validated_data):
        group_data = validated_data.pop('group')
        group, _ = Group.objects.get_or_create(**group_data)
        characteristics = validated_data.pop('characteristics')
        
        animal = Animal.objects.create(**validated_data, group=group)
        
        for characteristic in characteristics:
            characteristic, _ = Characteristic.objects.get_or_create(**characteristic)
            animal.characteristics.add(characteristic)
            
        return animal
    
    def update(self, instance, validated_data):
        not_updatable_fields = ['sex', 'group']
        
        for key, value in validated_data.items():
            if key in not_updatable_fields:
                raise KeyError({ "message": f"You can not update '{key}' property."}, status.HTTP_422_UNPROCESSABLE_ENTITY)
            
            if key == "characteristics":
                all_characteristics = []
                for characteristic in value:
                    char, _ = Characteristic.objects.get_or_create(**characteristic)
                    all_characteristics.append(char)
                instance.characteristics.set(all_characteristics)
            else:
                setattr(instance, key, value)
            
            instance.save()
            
        return instance