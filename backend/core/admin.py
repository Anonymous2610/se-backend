from django.contrib import admin

# Register your models here.
from .models import RoomNo, Customer, HouseKeeping, Analytics
admin.site.register(RoomNo)
admin.site.register(Customer)
admin.site.register(HouseKeeping)
admin.site.register(Analytics)

