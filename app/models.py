from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=False, help_text="Designates whether the user is a customer.")
    is_admin = models.BooleanField(default=False, help_text="Designates whether the user is an admin.")
    
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='customuser_groups',  
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='customuser_permissions', 
        blank=True
    )

    def __str__(self):
        return self.username

  
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)  
    description = models.TextField(null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"  # Proper plural form in admin
        ordering = ['name']  # Default ordering by name

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=255) 
    description = models.TextField(null=True, blank=True)  
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    stock = models.PositiveIntegerField(default=0)  
    image=models.ImageField(upload_to='image', blank=True, null=True)
    sizes = models.JSONField(null=True, blank=True)
    brand= models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    review = models.DecimalField(
        max_digits=3, decimal_places=2, null=True, blank=True
    ) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.name
    
# class Cart(models.model):
    