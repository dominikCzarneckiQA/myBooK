from django import forms
from .models import Post

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'url' , 'description')

        widgets = {
            'url': forms.HiddenInput
        }
