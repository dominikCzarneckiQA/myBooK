# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator

from django.views import View

from feed.models import Post
from .forms import LoginForm, UserRegisterForm, UserEditForm
from .models import Profile




def entryPageView(request):
    return render(request, 'entryPage.html', {})


def loginUserView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            gt = form.cleaned_data
            user = authenticate(username=gt['username'],
                                password=gt['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnienie zakończyło się sukcesem!')
                else:
                    return HttpResponse("Niestety. To konto jest zablokowane :(")
            else:
                return HttpResponse("Nieprawidłowe dane! Spróbuj ponownie. ")
    else:
        form = LoginForm()
    return render(request, 'konto/login.html', {'formularz': form})


#  widok rejestracyjny nowych użytkowników

def registerView(request):
    if request.method == 'POST':
        userForm = UserRegisterForm(request.POST)
        if userForm.is_valid():
            newUser = userForm.save(commit=False)
            newUser.set_password(
                userForm.cleaned_data['password1'])
            newUser.save()
            Profile.objects.create(user=newUser)

            return render(request, 'konto/register_success.html',
                          {'nowy_uzytkownik': newUser})
    else:
        userForm = UserRegisterForm()
    return render(request, 'konto/register.html',
                  {'user_form': userForm})


@login_required()
def editView(UpdateView):
    if UpdateView.method == 'POST':
        user_form = UserEditForm(instance=UpdateView.user, data=UpdateView.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=UpdateView.user)
    return render(UpdateView, 'konto/updateUser.html',
                  {
                   'user_form': user_form,
                   })


@method_decorator(login_required , name='dispatch')
class UserProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        getProfile = Profile.objects.get(pk=pk)
        getUser = getProfile.user
        getPosts = Post.objects.filter(postAuthor=getUser).order_by('-postDate')

        context = {
            'getUser': getUser,
            'getProfile': getProfile,
            'getPosts': getPosts,
        }
        return render(request, 'konto/userProfile.html', context)

@method_decorator(login_required , name='dispatch')
class ProfileUpdateView(View):
    model = Profile
    fields = ['profileAvatar', 'biography','birthDate', 'currentLocation', 'countryOrigin']