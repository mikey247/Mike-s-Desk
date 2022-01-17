
from multiprocessing import context
from django.shortcuts import render,get_object_or_404,redirect
from datetime import date
from blog.forms import CommentForm
from blog.models import Post,Author,Tag


# all_posts = [
  
# ]


def get_date(post):
    return post['date']



# Create your views here.

def index(request):
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:]
    
    latest_posts = Post.objects.all().order_by("-Date")[:3]
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
    
    return render(request, "blog/post-detail.html", {
        "post" : identified_post,
        "tags": identified_post.tags.all()
    } )

def comment(request):
    form = CommentForm(request.POST or None)

    if form.is_valid():
        print(form)
        form.save()
        return redirect('/')
    
    context={
        "form":form
    }
        
    return render(request, "blog/post-detail.html",context)