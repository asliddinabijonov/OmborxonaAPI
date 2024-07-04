from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated

from .serializers import *


class TarqatuvchiCreateAPIView(CreateAPIView):
    queryset = Tarqatuvchi.objects.all()
    serializer_class = TarqatuvchiPostSerializer


class TarqatuvchiRetieveAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Tarqatuvchi.objects.all()
    serializer_class = TarqatuvchiPostSerializer

    def get_object(self):
        return self.request.user
