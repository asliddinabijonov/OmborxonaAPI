from rest_framework import serializers

from user.models import *


class TarqatuvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarqatuvchi
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True},
        }


class TarqatuvchiPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarqatuvchi
        fields = ('username', 'password', 'tel', 'first_name', 'last_name', 'bolim', 'manzil')
        extra_kwargs = {
            'password': {'write_only': True},
            'tel': {'required': False},
            'first_name': {'required': False},
            'last_name': {'required': False},
            'bolim': {'required': False},
            'manzil': {'required': False},
        }

    def create(self, validated_data):
        return Tarqatuvchi.objects.create_user(**validated_data)
