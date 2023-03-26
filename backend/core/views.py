from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework import generics
from .models import RoomNo, Customer, HouseKeeping, Analytics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import authenticate
from .serializers import RoomNoSerializer, CustomerSerializer, HouseKeepingSerializer, AnalyticsSerializer
# Create your views here.

class LogInView(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            # login(request, user)
            return Response({"message": "Login successful"}, status=HTTP_200_OK)
        return Response({"message": "Invalid credentials"}, status=HTTP_400_BAD_REQUEST)


class RoomNoView(generics.ListCreateAPIView):
    queryset = RoomNo.objects.all()
    serializer_class = RoomNoSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)

class CustomerView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)

class HouseKeepingView(generics.ListCreateAPIView):
    queryset = HouseKeeping.objects.all()
    serializer_class = HouseKeepingSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)

class AnalyticsView(generics.ListCreateAPIView):
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
