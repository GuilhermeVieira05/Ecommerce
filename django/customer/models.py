from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    street = models.CharField(max_length=255)    
    number = models.CharField(max_length=20)     
    complement = models.CharField(max_length=100, blank=True, null=True)  
    district = models.CharField(max_length=100) 
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)      
    zip_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.street}, {self.number} - {self.city}/{self.state}"

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL, related_name='customer_address')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
