import self as self
from django import forms
from blog.models import Post, Comment, Category, Tag


class PostForm(forms.ModelForm):
    tags = forms.CharField()

    def save(self):
        saved_post = super().save()

        tag_list = []
        tags = self.cleaned_data.get("tags","")
        for word in tags.split(","):
            tag_name = word.strip()
            tag,__ = Tag.objects.get_or_create(name=tag_name)

            tag_list.append(tag)

        saved_post.tag_set.clear()
        saved_post.tag_set.add(*tag_list)
        return saved_post


    class Meta:
        model = Post
        fields = [
            "name",
            "content",
            "telephone",
            "status",
        ]
