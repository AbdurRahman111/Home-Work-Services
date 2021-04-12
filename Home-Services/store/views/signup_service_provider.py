from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
# from store.models.customer import Customer
from store.models.service_provider import ServiceProvider
from django.views import View


class Signup1(View):
    def get(self, request):
        return render(request, 'signup_service_provider.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        service_type = postData.get('service_type')

        aadhar = postData.get('aadhar')
        address = postData.get('address')
        area = postData.get('area')
        landmark = postData.get('landmark')
        pincode = postData.get('pincode')
        image = request.FILES['file_name']
        print("Image URL GETTING:",image)




        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,

            'aadhar': aadhar,
            'address': address,
            'area': area,
            'landmark': landmark,
            'pincode': pincode,
            'image': image,
        }
        error_message = None

        service_provider = ServiceProvider(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password,
                            service_type=service_type,

                            aadhar=aadhar,
                            address=address,
                            area=area,
                            landmark=landmark,
                            pincode=pincode,
                            image=image,
                            )
        error_message = self.validateServiceProvider(ServiceProvider)

        if not error_message:
            # print(first_name, last_name, phone, email, password)
            print('test')
            service_provider.password = make_password(service_provider.password)
            service_provider.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup_service_provider.html', data)

    def validateServiceProvider(self, service_provider):
        error_message = None
        if (not service_provider.first_name):
            error_message = "First Name Required !!"
        # elif len(service_provider.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not service_provider.last_name:
            error_message = 'Last Name Required'
        # elif len(service_provider.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not service_provider.phone:
            error_message = 'Phone Number required'
        # elif len(service_provider.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        # elif len(service_provider.password) < 6:
            error_message = 'Password must be 6 char long'
        # elif len(service_provider.email) < 5:
            error_message = 'Email must be 5 char long'
        # elif service_provider.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message
