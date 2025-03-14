from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from posts.models import Post
from users.forms import UserForm, RegisterForm, LoginForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
@staff_member_required
def admin_dashboard(request):
    users = User.objects.all()
    user_posts = [(user, Post.objects.filter(author=user)) for user in users]

    return render(request, 'users/admin_dashboard.html', {'user_posts':user_posts})

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html',{'users':users})

@login_required
@staff_member_required
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(author=user)

    return render(request, 'users/user_detail.html', {'user': user, 'posts': posts})


@login_required
def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request,'users/user_delete.html', {'user':user})

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have signed up successfully.')
            login(request, user)
            return redirect('posts')
        else:
            return render(request, 'users/register.html', {'form':form})

def user_login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('posts')

        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Check if user exists before authenticating
            User = get_user_model()
            try:
                user = User.objects.get(username=username)
                if not user.is_active:
                    messages.error(request, "Your account has been blocked! Please contact the administrator.")
                    return redirect('login')
            except User.DoesNotExist:
                user = None

            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, "Invalid username or password.")
                return redirect('login')

            # Successful login
            login(request, user)
            messages.success(request, f"Welcome back, {username.title()}!")
            return redirect('posts')

    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


@login_required
@staff_member_required
def toggle_user_status(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user.is_superuser:
        messages.error(request, "Bạn không thể khóa tài khoản admin!")
        return redirect('admin_dashboard')

    user.is_active = not user.is_active
    user.save()
    if user.is_active:
        messages.success(request, f"Tài khoản {user.username} đã được mở khóa.")
    else:
        messages.warning(request, f"Tài khoản {user.username} đã bị khóa.")
    return redirect('admin_dashboard')

