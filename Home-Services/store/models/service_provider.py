from django.db import models
from django.core.validators import MinLengthValidator

class ServiceProvider(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    service_type = models.CharField(max_length=200)

    aadhar = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    image = models.ImageField(upload_to='media/profiles/')
    date =models.DateTimeField(auto_now_add=True)

    def register(self):
        self.save()

    @staticmethod
    def get_service_provider_by_email(email):
        try:
            return ServiceProvider.objects.get(email=email)
        except:
            return False


    def isExists(self):
        if ServiceProvider.objects.filter(email = self.email):
            return True

        return  False
    
    

    def __str__(self):
        return self.first_name+ ' - ' +self.service_type


