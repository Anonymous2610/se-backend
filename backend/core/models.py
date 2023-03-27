from django.db import models

# Create your models here.
class RoomNo(models.Model):
    room_no = models.CharField(max_length=10)
    capacity = models.IntegerField(default=2)
    room_status=models.CharField(choices=[('available', 'Available'), ('not available', 'Not Available')], max_length=20, default='not available')
    def __str__(self):
        return self.room_no
 
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    room_no = models.ForeignKey(RoomNo, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField(blank=true)
    def __str__(self):
        return self.first_name

class HouseKeeping(models.Model):
    room_no = models.ForeignKey(RoomNo, on_delete=models.CASCADE)
    status = models.CharField(choices=[('clean', 'Clean'), ('dirty', 'Dirty')], max_length=10, default='dirty')
    inventory = models.CharField(choices=[('available', 'Available'), ('not available', 'Not Available')], max_length=20, default='not available')
    def __str__(self):
        call= "Room No: " + str(self.room_no)
        return call

class Analytics(models.Model):
    choices=[('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')]
    month = models.CharField(choices=choices, max_length=10)
    year = models.IntegerField(default=2023)
    expenditure = models.IntegerField(default=0)
    number_of_guests = models.IntegerField(default=0)


    def __str__(self):
        return self.month
