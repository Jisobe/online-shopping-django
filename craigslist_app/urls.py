from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.categories, name='categories'),
    path('posts', views.post_list, name='post-list'),
    path('posts/new', views.add_post, name='add-post'),
    path('categories/new', views.add_category, name='add-category'),
    path('categories/<int:category_id>', views.category_detail, name='category-detail'),
    path('categories/<int:category_id>/edit', views.edit_category, name='edit-category'),
    path('categories/<int:category_id>/posts/new', views.add_post_cat, name='add-post-cat'),
    path('categories/<int:category_id>/posts/<int:post_id>', views.post_detail, name='post-detail'),
    path('categories/<int:category_id>/posts/<int:post_id>/edit', views.edit_post, name='edit-post'),
]


# - `/categories`: A welcome page that lists all of the categories (with links to the categories)
# - `/categories/new`: A page with a form to create a new category
# - `/categories/<int:category_id>`: A page to view the detail of a specific category and a list of all of its associated posts (with links to those posts)
# - `/categories/<int:category_id>/edit`: A page with a form to update a specific category, **with current values filled in already**. Also include the ability to delete the specific category from here. 
# - `/categories/<int:category_id>/posts/new`: A page with a form to create a new post, **with the current category filled in already**.
# - `/categories/<int:category_id>/posts/<int:post_id>`: A page to view the detail of a specific post. Also include the ability go back to the parent category detail page (`/categories/<int:category_id/>`).
# - `/categories/<int:category_id>/posts/<int:post_id>/edit`: A page with a form to update a specific post, **with current values filled in already**. Also include the ability to delete the specific post from here.