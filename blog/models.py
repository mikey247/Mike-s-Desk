

from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator


# Create your models here.

class Author (models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField(max_length = 250)

    def __str__(self):
        return f"{self.First_name}, {self.Last_name}"



class Tag(models.Model):
    Caption = models.CharField(max_length=100)

    
    def __str__(self):
        return self.Caption
    

class UserComment(models.Model):
    name= models.CharField(max_length=100)
    comment = models.TextField(max_length=5000)

    def __str__(self):
        return self.name, self.comment
    


class Post(models.Model):
    Title = models.CharField(max_length=100)
    Excerpt = models.CharField(max_length=200)
    Image_name = models.CharField(max_length=50)
    Date= models.DateField(auto_now=True)
    slug= models.SlugField(unique=True,  db_index=True)
    Content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,null=True, related_name="posts")
    tags= models.ManyToManyField(Tag)
    comments=models.OneToOneField(UserComment,on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.Title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Title
    


