from django.shortcuts import render
from django.contrib.auth.models import User

from .serializers import RegSerializer,AllUserInformationSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

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
        return Response(serializer.errors)
    
class AllUserDetails(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = AllUserInformationSerializer