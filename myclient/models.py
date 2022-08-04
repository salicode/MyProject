from django.db import models
from graphene import ID

# Create your models here. 

STATUS_CHOICES = [
        ('NotStarted', 'Not Started'),
        ('InProgress', 'In Progress'),
        ('Completed', 'Completed'),
    ]


class Client(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    address = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    


class Contract(models.Model):
    
    contract_name = models.CharField(max_length=200, null=True)
    contract_type = models.CharField(max_length=200, null=True)
    contract_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Not Started')
    contract_description = models.TextField(max_length=1000, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    ID = models.ForeignKey(Client, max_length=250, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.contract_name








    
    
