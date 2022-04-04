from django import forms
from .models import Category, Post

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'description', 'price', 'contact_info', 'picture', 'category']