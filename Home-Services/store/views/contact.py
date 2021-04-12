from django.shortcuts import render, redirect
from django.views import *
from django.views import generic
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import UserCreateForm



def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["full_name"]} with email: {form.cleaned_data["email_address"]}'
            message = form.cleaned_data["message"]
            sender = 'home.services.on.demand03@gmail.com'
            recipients = ['home.services.on.demand03@gmail.com']
            try:
                print('test')
                send_mail(subject, message, sender, recipients)
                return HttpResponse('success message')
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('Success...Your email has been sent')
    return render(request, 'contact.html', {'form': form})



def signups(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('home')
    else:
        form = UserCreateForm()
    return render(request, 'login.html', {'form': form})
