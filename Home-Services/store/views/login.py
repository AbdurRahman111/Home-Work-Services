from django.shortcuts import render, redirect, HttpResponseRedirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.service_provider import ServiceProvider


class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        loginas = request.POST.get('loginas')
        if loginas == 'customer':
            print('customer')
            customer = Customer.get_customer_by_email(email)
            error_message = None
            if customer:
                flag = check_password(password, customer.password)
                if flag:
                    request.session['customer'] = customer.id
                    request.session['customer_phone'] = customer.phone
                    request.session['customer_first_name'] = customer.first_name
                    request.session['customer_last_name'] = customer.last_name
                    request.session['customer_email'] = customer.email

                    if Login.return_url:
                        print('test')
                        return HttpResponseRedirect(Login.return_url)
                    else:
                        Login.return_url = None
                        print('test2')
                        return redirect('homepage')
                else:
                    error_message = 'Email or Password invalid !!'
            else:
                error_message = 'Email or Password invalid !!'
        elif loginas == 'service':
            print('service')
            service_provider = ServiceProvider.get_service_provider_by_email(email)
            error_message = None
            if service_provider:
                print('service2')
                flag = check_password(password, service_provider.password)
                if flag:
                    request.session['customer'] = 'service_provider'
                    request.session['service_provider'] = service_provider.id
                    #request.session['service_provider'] = service_provider.id

                    if Login.return_url:
                        print('service3')
                        return HttpResponseRedirect(Login.return_url)
                    else:
                        print('service4')
                        Login.return_url = None
                        return redirect('orders')
                else:
                    error_message = 'Email or Password invalid !!'
            else:
                error_message = 'Email or Password invalid !!'
        # print(email, password)
        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')
