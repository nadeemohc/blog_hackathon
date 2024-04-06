from django.shortcuts import get_object_or_404, render, redirect
from .forms import BlogPostForm, CommentForm
from .models import BlogPost, Comment



def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('some_success_url')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})

def blog_post_detail(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    comments = Comment.objects.filter(blog_post=blog_post)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blog_post = blog_post
            comment.author = request.user
            comment.save()
            return redirect('blog_post_detail', blog_post_id=blog_post_id)  # Redirect to the same blog post detail page after successful comment submission
    else:
        comment_form = CommentForm()
    return render(request, 'blog_post_detail.html', {'blog_post': blog_post, 'comments': comments, 'comment_form': comment_form})
