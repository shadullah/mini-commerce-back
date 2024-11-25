from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout

from .serializers import RegSerializer,AllUserInformationSerializer,LoginSeria

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RegView(APIView):
    serializer_class = RegSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user=serializer.save()
            print(user)
            return Response("User registered successfull")
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    
class AllUserDetails(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = AllUserInformationSerializer


class loginView(APIView):
    def post(self, request):
        serializer = LoginSeria(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({"error": "User does not exists"})
            
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                access = refresh.access_token

                return Response({
                    'user': AllUserInformationSerializer(user).data,
                    'refreshToken': str(refresh),
                    'accessToken': str(access)
                }, status=status.HTTP_200_OK)
            
        return Response({'error':'invalid credentials'})
    
class logoutView(APIView):
    authentication_classes=[BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, req):
        try:
            logout(req)
            return Response({"success":"Logout success"})
        except:
            return Response({"error": "couldn\'t logout"})
