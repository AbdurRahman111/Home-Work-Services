from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
#from store.models.customer import Customer
from store.models.feedback import Feedback as fb
from store.models.orders import Order
from store.models.customer import Customer
from store.models.service_provider import ServiceProvider
from django.views import View
from store.forms import complete_order


def Feedback(request):
    if request.method=="POST":
        print('ok')
        completion_date = request.POST.get('completion_date')
        total_cost = request.POST.get('total_cost')

        Appointment_id = request.POST.get('Appointment_id')

        get_Order_data=Order.objects.get(id=Appointment_id)

        Service_provider_id = request.POST.get('Service_provider_id')
        Customer_id = request.POST.get('Customer_id')

        print(Service_provider_id, Customer_id)

        Service_provider_get=ServiceProvider.objects.get(id=Service_provider_id)
        Customer_get=Customer.objects.get(id=Customer_id)

        address = request.POST.get('address')
        Booking_date = request.POST.get('Booking_date')

        ins = fb(
            Appointment_id=Appointment_id,
            Service_provider_name=Service_provider_get,
            Customer_name=Customer_get,
            address=address,
            Booking_date=Booking_date,
            Completion_date=completion_date,
            Total_cost=total_cost,

            )
        ins.save()

        form2 = complete_order(request.POST, instance=get_Order_data)

        if form2.is_valid():
            form2.save()
            return redirect('orders')

        return redirect('orders')

    else:

        if request.session.get('customer') != 'service_provider':
            customer_full_name = request.session.get('customer')
            # print(customer_full_name)
            # orders = Order.get_orders_by_customer(customer)
            filter_fb = fb.objects.filter(Customer_name=customer_full_name)
            # print(filter_fb)
            context2 = {'filter_fb':filter_fb}
            return render(request, 'feedback.html', context2)

        elif request.session.get('customer') == 'service_provider':
            service_provider = request.session.get('service_provider')
            filter_fb = fb.objects.filter(Service_provider_name=service_provider)
            # print(filter_fb)
            context2 = {'filter_fb': filter_fb}
            return render(request, 'feedback.html', context2)









"""
class Feedback(View):
     def get(self, request):
         return render(request, 'feedback.html')

     def post(self, request):
         postData = request.POST
         serv_name = postData.get('serv_name')
         phone = postData.get('phone')
         email = postData.get('email')
         cust_name = postData.get('cust_name')
         address = postData.get('address')
         area = postData.get('area')
         pincode = postData.get('pincode')
         workstatus = postData.get('workstatus')

         ins = Feedback(serv_name=serv_name, phone=phone, email=email, cust_name=cust_name, address=address, area=area, pincode=pincode, workstatus=workstatus)
         ins.save()


         value = {
             'serv_name': serv_name,
             'phone': phone,
             'email': email,
             'cust_name': cust_name,
             'address': address,
             'area': area,
             'pincode': pincode,
             'workstatus': workstatus

         }
         error_message = None

         customer = Feedback(serv_name=serv_name,
                             phone=phone,
                             email=email,
                             cust_name=cust_name,
                             address=address,
                             area=area,
                             pincode=pincode,
                             workstatus=workstatus,
                             )
         customer.register()

         error_message = self.validateFeedback(customer)

         if not error_message:
              print(serv_name, phone, email, cust_name, address, area, pincode, workstatus)
              customer.password = make_password(customer.password)
              customer.register()
              return redirect('feedback')
         else:
             data = {
                 'error': error_message,
                 'values': value
             }
             return render(request, 'feedback.html', data)


    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
         #saving
   
       return error_message








 from django.shortcuts import render, redirect
 from django.contrib.auth.hashers import make_password
 from store.models.customer import Customer1
 from django.views import View


 class Customer1(View):
     def get(self, request):
         return render(request, 'feedback.html')

     def post(self, request):
         postData = request.POST
         service = postData.get('service')
         name = postData.get('name')
         total_price = postData.get('total_price')
         status = postData.get('status')

         # ins = Feedback(service=service, name=name, total_price=total_price, status=status)
         # ins.save()

         value = {
             'service': service,
             'name': name,
             'total_price': total_price,
             'status': status
         }
         error_message = None

         customer = Customer1(service=service,
                             name=name,
                             total_price=total_price,
                             status=status,
                             )
         # error_message = self.validateCustomer(customer)

         if not error_message:
             # print(first_name, last_name, phone, email, password)
             # customer.password = make_password(customer.password)
             customer.register()
             return redirect('homepage')
         else:
            data = {
                'error': error_message,
                 'values': value
             }
             return render(request, 'feedback.html', data)

    # def validateCustomer(self, customer):
    #     error_message = None
    #     if (not customer.first_name):
    #         error_message = "First Name Required !!"
    #     elif len(customer.first_name) < 4:
    #         error_message = 'First Name must be 4 char long or more'
    #     elif not customer.last_name:
    #         error_message = 'Last Name Required'
    #     elif len(customer.last_name) < 4:
    #         error_message = 'Last Name must be 4 char long or more'
    #     elif not customer.phone:
    #         error_message = 'Phone Number required'
    #     elif len(customer.phone) < 10:
    #         error_message = 'Phone Number must be 10 char Long'
    #     elif len(customer.password) < 6:
    #         error_message = 'Password must be 6 char long'
    #     elif len(customer.email) < 5:
    #         error_message = 'Email must be 5 char long'
    #     elif customer.isExists():
    #         error_message = 'Email Address Already Registered..'
    #      saving

         return error_message
"""

















































"""
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.feedback import Feedback
from django.views import View
from django.contrib import messages

def Feedback(request):
    if request.method=='POST':
        if request.POST.get('serv_name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('cust_name') and request.POST.get('address') and request.POST.get('area') and request.POST.get('pincode') and request.POST.get('workstatus'):
            details = feed()
            details.serv_name = request.POST.get('serv_name')
            details.phone = request.POST.get('phone')
            details.email = request.POST.get('email')
            details.cust_name = request.POST.get('cust_name')
            details.address = request.POST.get('address')
            details.area = request.POST.get('area')
            details.pincode = request.POST.get('pincode')
            details.workstatus = request.POST.get('workstatus')
            details.save()
            messages.success(request, 'Feedback Submitted!!!')
            return redirect('feedback')
    else:
        return redirect('feedback')







class Feedback(View):
    def get(self, request):
    	return render(request, 'feedback.html')



    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        phone = postData.get('phone')
        email = postData.get('email')
        cust_name = postData.get('custname')
        address = postData.get('address')
        area = postData.get('area')
        pincode = postData.get('pincode')
        work = postData.get('work')
        


        feedb = Feedback.objects().all()
        for i in feedb:
            i.serv_name=first_name
            i.phone=phone
            i.email=email
            i.cust_name=cust_name
            i.address=address
            i.area=area
            i.pincode=pincode
            i.workstatus=work
            i.save()
"""




        #feed = Feedback(serv_name=first_name, phone=phone, email=email, cust_name=cust_name, address=address, area=area, pincode=pincode, workstatus=work)
        #feed.save()
       # if Feedback.is_valid():
        #    Feedback.save()
        #else:
        #    return redirect('feedback')
"""
    value = {
    'first_name': firstname,
    'cust_name': custname,
    'phone': phone,
    'email': email,
    'custname': custname,
    'address': address,
    'area': area,
    'pincode': pincode,
    'work': work,
    }

    error_message = None

"""