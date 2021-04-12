from django.db import models
from django.core.validators import MinLengthValidator
from store.models.customer import Customer
from store.models.service_provider import ServiceProvider

class Feedback(models.Model):
    Appointment_id = models.CharField(max_length=200)
    Service_provider_name = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, default='1')
    Customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE, default='1')
    address = models.CharField(max_length=200)
    Booking_date = models.CharField(max_length=200)
    Completion_date = models.CharField(max_length=200)
    Total_cost = models.CharField(max_length=50)
    Review_Admin = models.BooleanField(default=False)


        