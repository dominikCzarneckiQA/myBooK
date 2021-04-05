from django import forms
from .models import Post, Comment


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['postContent', 'postImages']

        postImages = forms.ImageField(),
        widgets = {

            'postContent': forms.Textarea(attrs={'class': 'form-control ',
                                                 'rows': '2',
                                                 'placeholder': "Co u Ciebie?",
                                                 'style': 'resize:none'
                                                 }),



        }


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['commentContent']

        widgets = {

            'commentContent': forms.Textarea(attrs={'class': 'form-control',
                                                    'rows': '4',
                                                    'placeholder': 'Dodaj komentarz..',
                                                    'style': 'resize:none',

                                                    })
        }
