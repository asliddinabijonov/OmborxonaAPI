from django.urls import path
from .views import *

urlpatterns = [
    path('mahsulotlarfilter/', MahsulotlarAPIView.as_view()),
    path('mahsulotlar/', MahsulotlarListCreateAPIView.as_view()),
    path('mahsulotlar/<int:pk>/', MahsulotRetrieveUpdateDestroyAPIView.as_view()),
    path('mijozlar/', MijozlarAPIView.as_view()),
    path('mijozlar/<int:pk>/', MijozRetrieveUpdateDestroyAPIView.as_view()),
]
