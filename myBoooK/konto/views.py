# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LogForm, RejestracjaUzytkownika , EdycjaUzytkownika, EdycjaProfilu
from .models import Profile


# podstawowy widok zalogowanego użytkownika

#class HomePage(ListView):
 #   model = Wpis
  #  tempName = ''

def stronaWejsciowa(request):
    return render(request, 'stronaWejsciowa.html', {})

@login_required
def tablica(request):
    return render(request, 'dashboard.html',{'section': 'tablica'})

# widok logowania zarejestrowanego uzytkownika

def loginUzytkownik(request):
    if request.method == "POST":
        form = LogForm(request.POST)
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
        form = LogForm()
    return render(request, 'konto/login.html', {'form': form})

# utworzenie widoku rejestracji nowych użytkowników

def rejestracja(request):
    if request.method == 'POST':
        user_form = RejestracjaUzytkownika(request.POST)
        if user_form.is_valid():
            nowy_uzytkownik = user_form.save(commit=False)
            nowy_uzytkownik.set_password(user_form.cleaned_data['password'])
            nowy_uzytkownik.save()
            profile = Profile.objects.create(user=nowy_uzytkownik)
            return render(request, 'konto/register_done.html',{'nowy_uzytkownik': nowy_uzytkownik})
    else:
        user_form = RejestracjaUzytkownika
    return render(request, 'konto/register.html', {'user_form': user_form})

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
                   'profile_form':profile_form})