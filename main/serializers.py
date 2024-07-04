from rest_framework import serializers
from .models import Mahsulot, Mijoz


class MahsulotPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'

        extra_kwargs = {
            'narx2': {'required': False},
            'tarqatuvchi': {'required': False}
        }


class MahsulotUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = ('id', 'nom', 'brand', 'narx1', 'narx2', 'miqdor', 'olchov', 'sana')

        extra_kwargs = {
            'tarqatuvchi': {'read_only': False, 'required': False}
        }


class MijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'

        extra_kwargs = {
            'tarqatuvchi': {'read_only': False, 'required': False}
        }


class MijozUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = ('id', 'ism', 'dokon', 'tel', 'manzil', 'qarz')

        extra_kwargs = {
            'tarqatuvchi': {'read_only': False, 'required': False}
        }
