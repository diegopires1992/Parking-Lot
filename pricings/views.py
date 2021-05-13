from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PriceSerializers
from .models import Price

class PriciView(APIView):
    def post(self,request):
        serializer = PriceSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data
        price = Price.objects.create(**data)
        serializer = PriceSerializers(price)
        return Response(serializer.data,status=status.HTTP_201_CREATED)