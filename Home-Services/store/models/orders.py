from django.db import models
from .product import Product
from .customer import Customer
import datetime
from .service_provider import ServiceProvider





class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    service_provider = models.ForeignKey(ServiceProvider,on_delete=models.CASCADE,default=10)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    Service_date = models.CharField(max_length=50, default='', blank=True)
    Time_slots = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    complition_date = models.DateField(default=datetime.datetime.today)
    Accept_this_order = models.BooleanField(default=False)
    Cancel_this_order = models.BooleanField(default=False)
    Complete_this_order = models.BooleanField(default=False)


    def __str__(self):
        return self.product.name

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
    
    def get_orders_by_service_provider(service_provider_id):
        return Order.objects.filter(service_provider=service_provider_id).order_by('-date')

