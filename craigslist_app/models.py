from django.db import models
from djmoney.models.fields import MoneyField

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'Category: {self.name}'

class Post(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = MoneyField(max_digits=10, decimal_places=2, blank = True, null = True, default_currency='USD')
    contact_info = models.EmailField(max_length=100)
    picture = models.ImageField(blank = True, upload_to=None, height_field=None, width_field=None, max_length=None)
    post_date = models.DateField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, related_name= 'posts')

    def __str__(self):
        return f'Post: {self.name}'