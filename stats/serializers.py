from rest_framework import serializers
from .models import *


class SotuvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sotuv
        fields = ('id', 'mahsulot', 'mijoz', 'miqdor', 'summa', 'tolandi', 'qarz',)


class SotuvUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sotuv
        fields = ('id', 'mahsulot', 'mijoz', 'miqdor', 'summa', 'tolandi', 'qarz',)


