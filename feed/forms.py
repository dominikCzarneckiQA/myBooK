from django import forms
from .models import Post, Comment


class PostCreateForm(forms.ModelForm):
    postContent = forms.CharField(label='',
                                  widget=forms.Textarea(attrs={
                                      'class': 'form-control',
                                      'cols': '5',
                                      'placeholder': 'Co u Ciebie użytkowniku...?',
                                  }))

    class Meta:
        model = Post
        fields = ['postContent']


class CommentCreateForm(forms.ModelForm):
    commentContent = forms.CharField(label='',
                                     widget=forms.Textarea(attrs={

                                         'rows': '7',
                                         'class': 'form-control',
                                         'placeholder': 'Dodaj komentarz..'
                                     }))

    class Meta:
        model = Comment
        fields = ['commentContent']
