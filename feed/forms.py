from django import forms
from .models import Posts, Comments


class PostForm(forms.ModelForm):
    description = forms.CharField(label='',
                                  widget=forms.Textarea(attrs={
                                      'rows': '7',
                                      'cols': '77',
                                      'placeholder': 'Co u Ciebie Użytkowniku?'
                                  }))

    class Meta:
        model = Posts
        fields = ['description']


class CommentsForm(forms.ModelForm):
    comment = forms.CharField(label='',
                              widget=forms.Textarea(attrs={
                                  'rows': '7',
                                  'cols': '82',
                                  'placeholder': 'Dodaj komentarz..'
                              }))

    class Meta:
        model = Comments
        fields = ['comment']
