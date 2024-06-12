from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(null=True, blank=True, max_length=50, help_text="Name of our Clients or Customer")   
    customer_email = models.EmailField(null=True, blank=True, max_length=100, help_text="Email of our Clients or Customer")   
    customer_phone = models.CharField(null=True, blank=True, max_length=20, help_text="Phone Number of our Clients or Customer")   
    customer_address = models.CharField(null=True, blank=True, max_length=150, help_text="Address of our Clients or Customer")
    customer_category = models.CharField(null=True, blank=True, max_length=20, help_text="Category of our Client or Customer")
    customer_joined_yr = models.IntegerField(blank=True, null=True, help_text="Year when Client or Customer has joined us")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer_name} at {self.customer_joined_yr}"
    
    