from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product
import datetime

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        date_time = datetime.datetime.now()
        # print(date_time)
        return render(request , 'cart.html' , {'products' : products, 'date_time':date_time} )



