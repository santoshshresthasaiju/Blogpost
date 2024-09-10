from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User

# views for home page
@login_required
def home(request):
    return render(request, 'blogpost/home.html')

# views for post list
@login_required
def post_list(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    ) if query else Post.objects.select_related('author').prefetch_related('comments').all().order_by('-timestamp')

    # Pagination with dynamic adjustment of posts per page
    posts_per_page = request.GET.get('posts_per_page', 4)  # Default to 4
    paginator = Paginator(posts, posts_per_page)
    page_number = request.GET.get('page')
    
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blogpost/post_list.html', {'posts': posts, 'query': query})

# views for post creation
@login_required
def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('blogpost:post_list')
    else:
        post_form = PostForm()

    return render(request, 'blogpost/post_create.html', {'post_form': post_form})

# views for post update
@login_required
def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('blogpost:post_list')
    else:
        form = PostForm(instance=post)

    return render(request, 'blogpost/post_update.html', {'form': form, 'post': post})

# views for post detail with comments
@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('blogpost:post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()

    return render(request, 'blogpost/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })

# views for post deletion
@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    messages.success(request, 'Post deleted successfully!')
    return redirect('blogpost:post_list')

# views for comment deletion
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Allow either comment author or post author to delete the comment
    if request.user != comment.author and request.user != comment.post.author:
        messages.error(request, "You are not allowed to delete this comment.")
        return redirect(reverse('blogpost:post_detail', args=[comment.post.id]))

    comment.delete()
    messages.success(request, 'Comment deleted successfully!')
    return redirect(reverse('blogpost:post_detail', args=[comment.post.id]))

# views for user profile 
@login_required
def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts_list = Post.objects.select_related('author').prefetch_related('comments').filter(author=user).order_by('-timestamp')
    posts_per_page = request.GET.get('posts_per_page', 6)
    paginator = Paginator(posts_list, posts_per_page)
    page_number = request.GET.get('page')
    
    try:
        posts_list = paginator.page(page_number)
    except PageNotAnInteger:
        posts_list = paginator.page(1)
    except EmptyPage:
        posts_list = paginator.page(paginator.num_pages)
        
    return render(request, 'blogpost/user_profile.html', {'user': user, 'posts_list': posts_list})