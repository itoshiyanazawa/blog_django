from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Post, Comment  # Import Comment model

# Create your views here.
def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'blog/frontpage.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = post.comments.all()  # Fetch comments related to the post

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form, 'comments': comments})