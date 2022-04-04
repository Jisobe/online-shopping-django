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
