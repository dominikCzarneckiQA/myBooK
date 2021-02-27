from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import Profile

from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label='Potwierdz Haslo', widget=forms.PasswordInput)


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Haslo', widget=forms.PasswordInput(attrs={'class': 'form-control  '}))
    password2 = forms.CharField(label='Potwierdz Haslo', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}, ),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Niestety hasła nie są takie same!!")
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['biography', 'profileAvatar', 'birthDate', 'city', 'countryOrigin', 'github', 'snapchat',
                  'instagram', 'facebook', 'twitter']

        widgets = {

            'biography': forms.Textarea(attrs={'class': 'form-control ', }),
            'profileAvatar': forms.ImageField(),

            'birthDate': forms.DateField(widget=AdminDateWidget()),

            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'countryOrigin': forms.Select(attrs={'class': 'form-control'}),
            'github': forms.URLInput(attrs={'class': 'form-control'}),
            'snapchat': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control'}),
        }
