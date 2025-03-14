from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='posts'),
    path('my-posts/', views.my_posts, name='my_posts'),
    path('post/create', views.create_post, name='post-create'),
    path('post/edit/<int:id>', views.edit_post, name='post-edit'),
    path('post/delete/<int:id>', views.delete_post, name='post-delete'),
    path('about/',views.about, name='about'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
