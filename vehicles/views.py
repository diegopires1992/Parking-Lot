from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class VehiclesView(APIView):
    def post(self,request):
        return Response("teste")
