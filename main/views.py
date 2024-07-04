from rest_framework.generics import *
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import Mahsulot



class MahsulotlarListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotPostListSerializer

    def get_queryset(self):
        return self.queryset.filter(tarqatuvchi=self.request.user)

    def perform_create(self, serializer):
        serializer.save(tarqatuvchi=self.request.user)


class MahsulotRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotUpdateSerializer

    def get_queryset(self):
        return self.queryset.filter(tarqatuvchi=self.request.user)

    @swagger_auto_schema(
        request_body=MahsulotUpdateSerializer
    )
    def perform_update(self, serializer):
        serializer.save(tarqatuvchi=self.request.user)

    def perform_destroy(self, instance):
        if instance.tarqatuvchi == self.request.user:
            instance.delete()
            return Response(status=204)
        return Response(status=400)


class MijozlarAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mijozlar = Mijoz.objects.filter(tarqatuvchi=self.request.user)
        serializer = MijozSerializer(mijozlar, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=MijozUpdateSerializer
    )
    def post(self, request):
        serializer = MijozSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(tarqatuvchi=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class MijozRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Mijoz.objects.all()
    serializer_class = MijozUpdateSerializer

    def get_queryset(self):
        return self.queryset.filter(tarqatuvchi=self.request.user)

    @swagger_auto_schema(
        request_body=MijozUpdateSerializer
    )
    def perform_update(self, serializer):
        serializer.save(tarqatuvchi=self.request.user)

    def perform_destroy(self, instance):
        if instance.tarqatuvchi == self.request.user:
            instance.delete()
            return Response(status=204)
        return Response(status=400)
