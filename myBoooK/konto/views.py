# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LogowanieForm


# podstawowy widok logowania użytkownika

@login_required
def tablica(request):
    return render(request,
                  'dashboard.html',
                  {'section': 'tablica'})


def user_login(request):
    if request.method == "POST":
        form = LogowanieForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnienie zakończyło się sukcesem!')
                else:
                    return HttpResponse("Niestety. Te konto jest zablokowane :(")
            else:
                return HttpResponse("Nieprawidłowe dane! Spróbuj ponownie. ")
    else:
        form = LogowanieForm()
    return render(request, 'konto/login.html', {'form': form})