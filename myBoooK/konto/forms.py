from django import forms

class LogowanieForm(forms.Form):
    nazwaUzytkownika = forms.CharField()
    haslo = forms.CharField(widget=forms.PasswordInput)
