from django.urls import path
from .views import *

urlpatterns = [
    path('sotuv/', SotuvlarListCreateAPIView.as_view()),
    path('sotuv/<int:pk>/', SotuvRetrieveUpdateDestroyAPIView.as_view()),
]
