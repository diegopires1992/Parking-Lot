from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import AccountSerializers,CredentialSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status


class AccountView(APIView):
    def post(self,request):
        serializer = AccountSerializers(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        data = serializer.data
        user_exist = User.objects.filter(username=data["username"]).exists()

        if user_exist:
            return Response(status=status.HTTP_409_CONFLICT)

        user = User.objects.create_user(**data,password=request.data["password"])

        serializer = AccountSerializers(user)


        return Response(serializer.data,status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        serializer = CredentialSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=request.data["username"], password=request.data["password"])

        if user:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({"token": token.key})

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)