from rest_framework.serializers import ModelSerializer
from .models import RoomNo, Customer, HouseKeeping, Analytics

class RoomNoSerializer(ModelSerializer):
    class Meta:
        model = RoomNo
        fields = '__all__'

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class HouseKeepingSerializer(ModelSerializer):
    class Meta:
        model = HouseKeeping
        fields = '__all__'

class AnalyticsSerializer(ModelSerializer):
    class Meta:
        model = Analytics
        fields = '__all__'

