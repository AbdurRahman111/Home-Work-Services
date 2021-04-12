from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from store.forms import chg_status, cancel_status, complete_order


class OrderView(View):
    def get(self , request ):
        if request.session.get('customer') != 'service_provider':
            customer = request.session.get('customer')
            orders = Order.get_orders_by_customer(customer)

        elif request.session.get('customer') == 'service_provider':
            service_provider = request.session.get('service_provider')
            print(service_provider)

            orders = Order.get_orders_by_service_provider(service_provider)

        # print(orders)
        return render(request , 'orders.html' , {'orders' : orders})

def edit_order(request, pk):
    print('ss')
    get_order_by_id = Order.objects.get(id=pk)
    abc=get_order_by_id.id


    form = chg_status(instance=get_order_by_id)
    form1 = cancel_status(instance=get_order_by_id)

    if request.method == 'POST':
        print('nnn')
        form = chg_status(request.POST, instance=get_order_by_id)

        if form.is_valid():
            form.save()
            return redirect('orders')

    context={'form':form, 'form1':form1, 'abc':abc}
    return render(request, 'edit_order_status.html', context)


def cancel_order(request, pk):
    print('ok')
    get_order_by_id = Order.objects.get(id=pk)

    if request.method == 'POST':
        print('nnn')
        form1 = cancel_status(request.POST, instance=get_order_by_id)

        if form1.is_valid():
            form1.save()
            return redirect('orders')


def order_complete(request, pk):
    get_order_by_id = Order.objects.get(id=pk)
    form2 = complete_order(instance=get_order_by_id)

    context1={'get_order_by_id':get_order_by_id, 'form2':form2}
    return render(request, 'order_complete.html', context1)