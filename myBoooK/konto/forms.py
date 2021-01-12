from django import forms
from .models import Profile
from django.contrib.auth.models import User


class LogForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RejestracjaUzytkownika(forms.ModelForm):
    password1 = forms.CharField(label='Haslo ', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Potwierdz Haslo', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Niestety hasła nie są takie same!!")
        return cd['password2']

class EdycjaUzytkownika(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class EdycjaProfilu(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
