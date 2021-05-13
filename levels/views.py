from rest_framework import serializers
from rest_framework.response import Response
from .models import Level
from rest_framework.views import APIView
from .serializers import LevelSerializers,AvaliableSerializers
from rest_framework import status
from .models import Avaliable,Level


class LevelView(APIView):
    def post(self,request):
        serializer = LevelSerializers(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
              
        leveldata = serializer.data
        avaliable = Avaliable.objects.get_or_create(avaliable_motorcycle_spaces=request.data['motorcycle_spaces'],avaliable_car_spaces=request.data['car_spaces'])
        level = Level.objects.get_or_create(name=leveldata['name'],fill_priority=leveldata['fill_priority'],avaliable_spaces=avaliable[0])
        
        serializer = LevelSerializers(level[0])

        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def get(self,request):
        queryset = Level.objects.all()
        serializer = LevelSerializers(queryset,many=True)
        return Response(serializer.data)
    

