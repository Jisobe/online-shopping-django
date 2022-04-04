from django.shortcuts import redirect, render, reverse
from django.http import HttpResponse
from .models import Category, Post
from django.core.exceptions import ValidationError

# A welcome page that lists all of the categories (with links to the categories)
def categories(request):
    category_list= {}
    category_list['category_names'] = Category.objects.all()
    return render(request, 'pages/categories.html', category_list)

# A page that lists all of the posts
def post_list(request):
    post_list= {}
    post_list['posts'] = Post.objects.all()
    return render(request, 'pages/all_posts.html', post_list)

# A page to add a post to any category
def add_post(request):
    my_data = {}
    my_data['categories'] = Category.objects.all()
    if request.method == 'POST':
        try:
            post = Post()
            post.name = request.POST['post-name']
            post.description = request.POST['post-detail']
            post.price = request.POST['post-price']
            post.contact_info = request.POST['post-contact']
            post.picture = request.POST['post-picture']
            post.category.id = request.POST['post-category']
            post.full_clean()
            post.save()
        except ValidationError as ve:
            my_data['error'] = ve.message_dict
    return render(request, 'pages/add_post.html', my_data)

# A page with a form to create a new category
def add_category(request):
    my_data = {}
    if request.method == 'POST':
        try:
            category = Category()
            category.name = request.POST['category-name']
            category.description = request.POST['category-detail']
            category.full_clean()
            category.save()
        except ValidationError as ve:
            my_data['error'] = ve.message_dict
    return render(request, 'pages/add_category.html', my_data)

# A page to view the detail of a specific category and a list of all of its associated posts (with links to those posts)
def category_detail(request, category_id):
    my_data = {}
    my_data['category'] = Category.objects.get(pk=category_id)
    return render(request, 'pages/category_detail.html', my_data)

# A page with a form to update a specific category, **with current values filled in already**. Also include the ability to delete the specific category from here. 
def edit_category(request, category_id):
    my_data = {}
    my_data['category'] = Category.objects.get(pk=category_id)
    if request.method == 'POST':
        delete = 'delete_category' in request.POST
        try:
            if delete:
                category_to_delete = request.POST['delete_category']
                Category.objects.get(pk=category_to_delete).delete()
                return redirect(reverse('categories'))
            else:
                category = Category.objects.get(pk = category_id)
                category.name = request.POST['name']
                category.description = request.POST['detail']
                category.full_clean()
                category.save()
                return redirect(reverse('category-detail', args=(category_id, )))
        except ValidationError as ve:
            my_data['error'] = ve.message_dict
    return render(request, 'pages/edit_category.html', my_data)

# A page with a form to create a new post, **with the current category filled in already**.
def add_post_cat(request, category_id):
    my_data = {}
    my_data['category'] = Category.objects.get(pk=category_id)
    my_data['categories'] = Category.objects.all()
    if request.method == 'POST':
        try:
            post = Post()
            category = Category.objects.get(pk=request.POST['post-category'])
            post.name = request.POST['post-name']
            post.description = request.POST['post-detail']
            post.price = request.POST['post-price']
            post.contact_info = request.POST['post-contact']
            post.picture = request.POST['post-picture']
            post.full_clean()
            post.save()
            post.category.add(category)
        except ValidationError as ve:
            my_data['error'] = ve.message_dict
    return render(request, 'pages/add_post_cat.html', my_data)

# A page to view the detail of a specific post. Also include the ability go back to the parent category detail page (`/categories/<int:category_id/>`).
def post_detail(request, category_id, post_id):
    post_list = {}
    post_list['post'] = Post.objects.get(pk = post_id)
    post_list['category'] = Category.objects.get(pk = category_id)
    return render(request, 'pages/post_detail.html', post_list)

# A page with a form to update a specific post, **with current values filled in already**. Also include the ability to delete the specific post from here.
def edit_post(request, category_id, post_id):
    my_data = {}
    my_data['post'] = Post.objects.get(pk=post_id)
    my_data['categories'] = Category.objects.all()
    if request.method == 'POST':
        delete = 'delete_post' in request.POST
        try:
            if delete:
                post_to_delete = request.POST['delete_post']
                Post.objects.get(pk=post_to_delete).delete()
                return redirect(reverse('category-detail', args=(category_id, )))
            else:
                post = Post.objects.get(pk = post_id)
                category = Category.objects.get(pk=request.POST['post_category'])
                post.name = request.POST['post_name']
                post.description = request.POST['post_detail']
                post.price = request.POST['post_price']
                post.contact_info = request.POST['post_contact']
                post.picture = request.POST['post_picture']
                post.full_clean()
                post.save()
                post.category.add(category)
                return redirect(reverse('post-detail', args=(category_id, post_id, )))
        except ValidationError as ve:
            my_data['error'] = ve.message_dict

    return render(request, 'pages/edit_post.html', my_data)
