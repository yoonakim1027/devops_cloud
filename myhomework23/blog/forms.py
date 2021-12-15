from django import forms
from blog.models import Post, Comment, Category, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "name",
            "content",
            "telephone",
            "status",
        ]
