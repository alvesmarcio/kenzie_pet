from django.urls import path

from .views import AnimalView, AnimalIdView

urlpatterns = [
    path('animals/', AnimalView.as_view()),
    path('animals/<int:animal_id>/', AnimalIdView.as_view()),
]