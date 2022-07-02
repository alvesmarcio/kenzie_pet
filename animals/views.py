from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from .models import Animal
from .serializers import AnimalSerializer

class AnimalView(APIView):
    def get(self, _: Request) -> Response:
        animals = Animal.objects.all()
        serialized = AnimalSerializer(animals, many=True)
        
        return Response({"animals": serialized.data},status=status.HTTP_200_OK)
    
    def post(self, request: Request) -> Response:
        serialized = AnimalSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    
class AnimalIdView(APIView):
    def get(self, _: Request, animal_id: int) -> Response:
        animal = get_object_or_404(Animal, id=animal_id)
        serialized = AnimalSerializer(animal)
        
        return Response({"animal": serialized.data}, status=status.HTTP_200_OK)
    
    def patch(self, request: Request, animal_id: int) -> Response:
        animal = get_object_or_404(Animal, id=animal_id)
        serialized = AnimalSerializer(animal, data=request.data, partial=True)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def delete(self, _: Request, animal_id: int) -> Response:
        animal = get_object_or_404(Animal, id=animal_id)
        animal.delete()
        serialized = AnimalSerializer(animal)
        
        return Response(serialized.data, status=status.HTTP_200_OK)