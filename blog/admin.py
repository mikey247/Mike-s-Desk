from django.contrib import admin
from blog.models import Post,Author,Tag,UserComment

class PostAdmin(admin.ModelAdmin):
    list_filter=("author", "tags", "Date")
    list_display=("Title", "Date", "author")
    # prepopulated_fields = {"slug": ("Title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


# Register your models here.

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(UserComment,CommentAdmin)