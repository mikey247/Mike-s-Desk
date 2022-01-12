from django.shortcuts import render
from datetime import date


all_posts = [
    {
        "slug": "new-beginnings",
        "image" : "kobe.jpg",
        "author": "Michael Umeokoli",
        "date" : date(2022,1,9),
        "title" : "NEW BEGINNINGS !!!!!",
        "excerpt": "There is always some confusion when  going into a new field especially in the world of tech, so many career paths, information, tools and terminologies are out there and this can easily overwhelm anybody, what i always try to do is break these information into bits...'",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo error dicta rem nostrum aut velit temporibus cupiditate sunt provident eius porro veniam dolore, illo eligendi aliquam voluptates illum doloribus dolorem!         Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo error dicta rem nostrum aut velit temporibus cupiditate sunt provident eius porro veniam dolore, illo eligendi aliquam voluptates illum doloribus dolorem!         Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo error dicta rem nostrum aut velit temporibus cupiditate sunt provident eius porro veniam dolore, illo eligendi aliquam voluptates illum doloribus dolorem!
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo error dicta rem nostrum aut velit temporibus cupiditate sunt provident eius porro veniam dolore, illo eligendi aliquam voluptates illum doloribus dolorem!
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo error dicta rem nostrum aut velit temporibus cupiditate sunt provident eius porro veniam dolore, illo eligendi aliquam voluptates illum doloribus dolorem!
        """
    },

     {
        "slug": "staying-grounded",
        "image" : "dr-j.jpg",
        "author": "Michael Umeokoli",
        "date" : date(2021,11,9),
        "title" : "STAYING GROUNDED",
        "excerpt": "There is always some confusion when  going into a new field especially in the world of tech, so many career paths, information, tools and terminologies are out there and this can easily overwhelm anybody, what i always try to do is break these information into bits...'"
        ,"content" : """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo error dicta rem nostrum aut velit temporibus cupiditate sunt provident eius porro veniam dolore, illo eligendi aliquam voluptates illum doloribus dolorem!         Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo error dicta rem nostrum aut velit temporibus cupiditate sunt provident eius porro veniam dolore, illo eligendi aliquam voluptates illum doloribus dolorem!         Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo error dicta rem nostrum aut velit temporibus cupiditate sunt provident eius porro veniam dolore, illo eligendi aliquam voluptates illum doloribus dolorem!
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo error dicta rem nostrum aut velit temporibus cupiditate sunt provident eius porro veniam dolore, illo eligendi aliquam voluptates illum doloribus dolorem!
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo error dicta rem nostrum aut velit temporibus cupiditate sunt provident eius porro veniam dolore, illo eligendi aliquam voluptates illum doloribus dolorem!
        """
    },

     {
        "slug": "programming-is-hard",
        "image" : "mj-kobe.jpg",
        "author": "Michael Umeokoli",
        "date" : date(2021,12,6),
        "title" : "Programming is Hard !!!",
        "excerpt": "There is always some confusion when  going into a new field especially in the world of tech, so many career paths, information, tools and terminologies are out there and this can easily overwhelm anybody, what i always try to do is break these information into bits...'",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo error dicta rem nostrum aut velit temporibus cupiditate sunt provident eius porro veniam dolore, illo eligendi aliquam voluptates illum doloribus dolorem!         Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo error dicta rem nostrum aut velit temporibus cupiditate sunt provident eius porro veniam dolore, illo eligendi aliquam voluptates illum doloribus dolorem!         Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo error dicta rem nostrum aut velit temporibus cupiditate sunt provident eius porro veniam dolore, illo eligendi aliquam voluptates illum doloribus dolorem!
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo error dicta rem nostrum aut velit temporibus cupiditate sunt provident eius porro veniam dolore, illo eligendi aliquam voluptates illum doloribus dolorem!
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo error dicta rem nostrum aut velit temporibus cupiditate sunt provident eius porro veniam dolore, illo eligendi aliquam voluptates illum doloribus dolorem!
        """
        

    }
]


def get_date(post):
    return post['date']

# Create your views here.

def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
       "posts": latest_posts
    } )

def posts(request):
    return render(request, "blog/all-posts.html" , {
        "all_posts": all_posts
    } )

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug']==slug)
    return render(request, "blog/post-detail.html", {
        "post" : identified_post
    } )