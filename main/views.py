from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Mahsulot
from .serializers import MahsulotSerializer


class MahsulotlarAPIView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            mahsulotlar = Mahsulot.objects.all()
            serializer = MahsulotSerializer(mahsulotlar, many=True)
            return Response(serializer.data, status=200)

        return Response(status=401)
