from django import forms
from .models import Post, Comment


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['postContent', 'postImages']

        widgets = {
            'postContent': forms.Textarea(attrs={'class': 'form-control ',
                                                 'rows': '2',
                                                 'placeholder': 'Dodaj komentarz..'
                                                 }),

        }


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['commentContent']

        commentContent = forms.CharField(label='',
                                         widget=forms.Textarea(attrs={

                                             'rows': '7',
                                             'class': 'form-control',
                                             'placeholder': 'Dodaj komentarz..'
                                         }))
