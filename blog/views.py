
from multiprocessing import context
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView
from datetime import date
from blog.forms import CommentForm
from blog.models import Post,Author,Tag


# all_posts = [
  
# ]


def get_date(post):
    return post['date']



# Create your views here.

def index(request):
    latest_posts = Post.objects.all().order_by("-Date")[:5]
    return render(request, "blog/index.html", {
       "posts": latest_posts
    } )

def posts(request):
    all_posts= Post.objects.all().order_by("-Date")
    return render(request, "blog/all-posts.html" , {
        "all_posts": all_posts
    } )

def post_detail(request, slug):
    # identified_post= get_object_or_404(Post,slug=slug)
    identified_post = Post.objects.get(slug=slug)
    comments = identified_post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = identified_post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    return render(request, "blog/post-detail.html", {
        "post" : identified_post,
        "tags": identified_post.tags.all(),
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    } )