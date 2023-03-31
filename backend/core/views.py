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

    
class HomeView(APIView):
    def get(self, request):
        user = request.user
        context = {}
        if user.is_authenticated:
            if (user.is_superuser):
                Customer_list = Customer.objects.all()
                analytics = Analytics.objects.all()
                context['Customer_list'] = CustomerSerializer(Customer_list, many=True).data
                context['analytics'] = AnalyticsSerializer(analytics, many=True).data
                return Response(context, status=HTTP_200_OK)
            elif(user.is_staff):
                room_list = RoomNo.objects.all()
                
                context['room_list'] = RoomNoSerializer(room_list, many=True).data
                housekeeping_list = HouseKeeping.objects.all()
                context['housekeeping_list'] = HouseKeepingSerializer(housekeeping_list, many=True).data
                return Response(context, status=HTTP_200_OK)
                return Response({"message": "Hello, User!"}, status=HTTP_200_OK)
        return Response({"message": "Log in First!!"}, status=HTTP_400_BAD_REQUEST)
