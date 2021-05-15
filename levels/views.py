from rest_framework import serializers
from rest_framework.response import Response
from .models import Level
from rest_framework.views import APIView
from .serializers import LevelSerializers,AvaliableSerializers
from rest_framework import status
from .models import Avaliable,Level
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class LevelView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = LevelSerializers(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
              
        leveldata = serializer.data
        available = Avaliable.objects.create(available_motorcycle_spaces=request.data['motorcycle_spaces'],available_car_spaces=request.data['car_spaces'])
        level = Level.objects.create(name=leveldata['name'],fill_priority=leveldata['fill_priority'],available_spaces=available)
        
        serializer = LevelSerializers(level)

        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def get(self,request):
        queryset = Level.objects.all()
        serializer = LevelSerializers(queryset,many=True)
        return Response(serializer.data)
    

