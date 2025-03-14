from django.urls import path
from . import views

urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/users/', views.user_list, name='user_list'),
    path('admin-dashboard/toggle-user-status/<int:user_id>/', views.toggle_user_status, name='toggle_user_status'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('admin-dashboard/users/delete/<int:user_id>/', views.user_delete, name='user_delete'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
