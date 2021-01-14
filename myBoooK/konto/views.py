# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LogForm, RejestracjaUzytkownika , EdycjaUzytkownika, EdycjaProfilu
from .models import Profile

# widok
def stronaStartowa(request):
    return render(request, 'stronaStartowa.html', {})

# podstawowy widok tablicy zalogowanego uzytkownika
@login_required
def tablica(request):
    return render(request, 'stronaTablica.html', {'section': 'tablica'})

# widok logowania zarejestrowanego uzytkownika

def loginUzytkownik(request):
    if request.method == "POST":
        formularz = LogForm(request.POST)
        if formularz.is_valid():
            gt = formularz.cleaned_data
            user = authenticate(username=gt['username'],
                                password=gt['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnienie zakończyło się sukcesem!')
                else:
                    return HttpResponse("Niestety. Te konto jest zablokowane :(")
            else:
                return HttpResponse("Nieprawidłowe dane! Spróbuj ponownie. ")
    else:
        formularz = LogForm()
    return render(request, 'konto/zaloguj.html', {'formularz': formularz})

# utworzenie widoku rejestracji nowych użytkowników

def rejestracja(request):
    if request.method == 'POST':
        uzytkownik_form = RejestracjaUzytkownika(request.POST)
        if uzytkownik_form.is_valid():
            nowy_uzytkownik = uzytkownik_form.save(commit=False)
            nowy_uzytkownik.set_password(
                uzytkownik_form.cleaned_data['haslo'])
            nowy_uzytkownik.save()
            Profile.objects.create(user=nowy_uzytkownik)
            return render(request, 'konto/rejestracja_gotowe.html',
                          {'nowy_uzytkownik': nowy_uzytkownik})
    else:
        uzytkownik_form = RejestracjaUzytkownika()
    return render(request, 'konto/register.html',
                  {'uzytkownik_form': uzytkownik_form})

@login_required()
def edycja(request):
    if request.method == 'POST':
        user_form = EdycjaUzytkownika(instance=request.user, data=request.POST)
        profile_form = EdycjaProfilu(instance=request.user, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = EdycjaUzytkownika(instance=request.user)
        profile_form = EdycjaProfilu(instance=request.user)
    return render(request, 'konto/edycja.html',
                  {'user_form': user_form,
                   'profile_form':profile_form
                   })
