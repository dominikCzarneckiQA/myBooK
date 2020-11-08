# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LogowanieForm

# podstawowy widok logowania użytkownika

def logowanie_uzytkownik(request):
    if request.method == "POST":
        formularz = LogowanieForm(request.POST)
        if formularz.is_valid():
            cd = formularz.cleaned_data
            user = authenticate(username=cd['nazwauzytko'],
                                password=cd['haslo'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Hurra! Uwierzytelnienie pomyślne! :]')
                else:
                    return HttpResponse("Niestety. Te konto jest niedostępne! :<")
            else:
                return HttpResponse("Przykro mi.. Te dane są nieprawidłowe :(")
    else:
        formularz = LogowanieForm()
    return render(request, 'konto/login.html', {'form': formularz})
