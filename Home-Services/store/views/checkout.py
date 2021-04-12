from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from datetime import datetime, timedelta
from store.models.product import Product
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        order_date = request.POST.get('order_date')
        radio_btn = request.POST.get('radio_btn')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(order_date, radio_btn, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            completion_date = datetime.now() + timedelta(days=product.complition_time)
            order = Order(customer=Customer(id=customer),
                          product=product,
                          service_provider=product.service_provider,
                          price=product.price,
                          Service_date=order_date,
                          Time_slots=radio_btn,
                          complition_date = completion_date,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')
