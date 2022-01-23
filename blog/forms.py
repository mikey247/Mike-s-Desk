from django.forms import ModelForm
from blog.models import UserComment

class CommentForm(ModelForm):
    class Meta:
        model = UserComment
        fields = ('name', 'email', 'body')