from django import forms
from .models import Post, Comment


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['postContent']

    postContent = forms.CharField(label='',
                                  widget=forms.TextInput(attrs={
                                      'class': 'form-control',
                                      'cols': '11',

                                      'placeholder': 'Co u Ciebie użytkowniku...?',
                                  }))


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
