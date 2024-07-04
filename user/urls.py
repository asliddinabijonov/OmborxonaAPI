from django.urls import path
from .views import *

urlpatterns = [
    path('register/', TarqatuvchiCreateAPIView.as_view()),
    path('details/', TarqatuvchiRetieveAPIView.as_view())
]
