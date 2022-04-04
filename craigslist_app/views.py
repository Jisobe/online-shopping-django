from django.shortcuts import redirect, render, reverse
from .models import Category, Post
from .forms import CategoryForm, PostForm

# A welcome page that lists all of the categories (with links to the categories)
def categories(request):
    category_list= {}
    category_list['category_names'] = Category.objects.all()
    return render(request, 'pages/categories.html', category_list)

# A page that lists all of the posts
def post_list(request):
    post_list= {}
    post_list['categories'] = Category.objects.all()
    post_list['posts'] = Post.objects.all()
    return render(request, 'pages/all_posts.html', post_list)

# A page to add a post to any category
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            category = Category.objects.get(pk=request.POST['category'])
            post = form.save(commit=False)
            post.save()
            post.category.add(category)
            return redirect(reverse('categories'))
    else:
        post = PostForm()
        my_data = {
            'post': post,
            'type_of_request': 'New'
        }
        return render(request, 'pages/add_post.html', my_data)

# A page with a form to create a new category
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            category.save()
            return redirect(reverse('categories'))
    else:
        category = CategoryForm()
        my_data = {
            'category': category,
            'type_of_request': 'New'
        }
        return render(request, 'pages/add_category.html', my_data)

# A page to view the detail of a specific category and a list of all of its associated posts (with links to those posts)
def category_detail(request, category_id):
    my_data = {}
    my_data['category'] = Category.objects.get(pk=category_id)
    return render(request, 'pages/category_detail.html', my_data)

# A page with a form to update a specific category, **with current values filled in already**. Also include the ability to delete the specific category from here. 
def edit_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    if request.method == 'POST':
        delete = 'delete_category' in request.POST
        if delete:
            category = Category.objects.get(pk=category_id)
            category.delete()
            return redirect('categories')       
        else:     
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                category = form.save(commit=False)
                category.save()
                return redirect(reverse('categories'))
    else:
        category = CategoryForm(instance=category)
        my_data = {
            'category': category,
            'type_of_request': 'Edit'
        }
        return render(request, 'pages/edit_category.html', my_data)

# A page with a form to create a new post, **with the current category filled in already**.
def add_post_cat(request, category_id):
    category = Category.objects.get(pk=category_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            category = Category.objects.get(pk=request.POST['category'])
            post = form.save(commit=False)
            post.save()
            post.category.add(category)
            return redirect(reverse('categories'))
    else:
        post = PostForm()
        my_data = {
            'post': post,
            'type_of_request': 'New'
        }
        return render(request, 'pages/add_post.html', my_data)

# A page to view the detail of a specific post. Also include the ability go back to the parent category detail page (`/categories/<int:category_id/>`).
def post_detail(request, category_id, post_id):
    post_list = {}
    post_list['post'] = Post.objects.get(pk = post_id)
    post_list['category'] = Category.objects.get(pk = category_id)
    return render(request, 'pages/post_detail.html', post_list)

# A page with a form to update a specific post, **with current values filled in already**. Also include the ability to delete the specific post from here.
def edit_post(request, category_id, post_id):
    category = Category.objects.get(pk=category_id)
    post=Post.objects.get(pk=post_id)
    if request.method == 'POST':
        delete = 'delete_post' in request.POST
        if delete:
            post = Post.objects.get(pk=post_id)
            post.delete()
            return redirect(reverse('category-detail', args=(category_id, )))       
        else:     
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect(reverse('post-detail', args=(category.id, post.id, )))
    else:
        post = PostForm(instance=post)
        my_data = {
            'post': post,
            'type_of_request': 'Edit'
        }
        return render(request, 'pages/edit_post.html', my_data)
