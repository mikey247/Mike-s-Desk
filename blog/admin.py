from django.contrib import admin
from blog.models import Post,Author,Tag,UserComment

class PostAdmin(admin.ModelAdmin):
    list_filter=("author", "tags", "Date")
    list_display=("Title", "Date", "author")
    # prepopulated_fields = {"slug": ("Title",)}

# Register your models here.

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(UserComment)