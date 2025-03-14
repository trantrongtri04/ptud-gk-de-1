from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm, CommentForm


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)

    # Kiểm tra xem user có phải là tác giả bài viết không
    if post.author != request.user:
        messages.error(request, "You don't have permission to delete this post.")
        return redirect('posts')

    context = {'post': post}

    if request.method == 'GET':
        return render(request, 'blog/post_confirm_delete.html', context)
    
    elif request.method == 'POST':
        post.delete()
        messages.success(request, 'The post has been deleted successfully.')
        return redirect('posts')


@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    # Kiểm tra quyền sở hữu
    if post.author != request.user:
        messages.error(request, "You don't have permission to edit this post.")
        return redirect('posts')

    if request.method == 'GET':
        context = {'form': PostForm(instance=post), 'id': id}
        return render(request, 'blog/post_form.html', context)

    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/post_form.html', {'form': form})

        
@login_required
def create_post(request):
    if request.method == 'GET':
        context = {'form':PostForm()}
        return render(request, 'blog/post_form.html',context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/post_form.html',{'form':form})
        
    
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html',{'posts':posts, 'filter':True})

def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/home.html',{'posts':posts, 'filter':False})

def about(request):
    return render(request, 'blog/about.html')

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()  # Lấy danh sách bình luận của bài viết
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.success(request, 'Your comment has been added!')
            return redirect('post_detail', id=post.id)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})


def dashboard(request):
    total_posts = Post.objects.count()
    latest_posts = Post.objects.order_by('-created_at')[:5]
    context = {
        'total_posts': Post.objects.count(),
        'latest_posts': latest_posts,
    }
    return render(request, 'blog/dashboard.html', context)