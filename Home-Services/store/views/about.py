from django.shortcuts import render, redirect , HttpResponseRedirect

from store.models.customer import Customer
from django.views import View
from django.shortcuts import render, redirect


class About(View):
    return_url = None
    def get(self , request):
        return render(request, 'about.html')

