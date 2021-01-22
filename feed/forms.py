from django import forms
from .models import Post


class postForm(forms.ModelForm):
    description = forms.CharField(label='',
                                  widget=forms.Textarea(attrs={

                                      'rows': '7',
                                      'cols': '77',
                                      'placeholder': 'Co u Ciebie Użytkowniku?'
                                  }))

    class Meta:
        model = Post
        fields = ['description']

