from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'blogpost/home.html')

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blogpost/post_list.html', {'posts':posts})

@login_required
def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('blogpost:post_list')
    else:
        post_form = PostForm()
    return render(request, 'blogpost/post_create.html', {'post_form':post_form})

@login_required
def post_detail(request, post_id):
    post =  Post.objects.get(id=post_id)
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
        'post':post,
        'comments': comments,
        'comment_form': comment_form
        })        

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author == request.user:
        comment.delete()
        return redirect('blogpost:post_detail', post_id=comment.post.id)
