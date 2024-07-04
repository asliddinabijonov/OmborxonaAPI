from rest_framework.generics import *
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class SotuvlarListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Sotuv.objects.all()
    serializer_class = SotuvSerializer

    def get_queryset(self):
        return self.queryset.filter(tarqatuvchi=self.request.user)

    @swagger_auto_schema(
        request_body=SotuvUpdateSerializer
    )
    def perform_create(self, serializer):
        serializer.save(tarqatuvchi=self.request.user)

class SotuvRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Sotuv.objects.all()
    serializer_class = SotuvUpdateSerializer

    def get_queryset(self):
        return self.queryset.filter(tarqatuvchi=self.request.user)

    @swagger_auto_schema(
        request_body=SotuvUpdateSerializer
    )
    def perform_update(self, serializer):
        serializer.save(tarqatuvchi=self.request.user)

    def perform_destroy(self, instance):
        if instance.tarqatuvchi == self.request.user:
            instance.delete()
            return Response(status=204)
        return Response(status=400)
