# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from django.views import View

from feed.models import Post
from .forms import LoginForm, UserRegisterForm, UserEditForm, ProfileUpdateForm
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
def editView(request):
    if request.method == 'POST':
        userForm = UserEditForm(instance=request.user, data=request.POST)
        if userForm.is_valid():
            userForm.save()
    else:
        userForm = UserEditForm(instance=request.user)
    return render(request, 'konto/updateUser.html',
                  {
                      'userForm': userForm,
                  })


@method_decorator(login_required, name='dispatch')
class UserProfileView(View):
    def get(self, request, pk, *args, **kwargs):

        global is_friend
        getProfile = Profile.objects.get(pk=pk)
        getUser = getProfile.user
        getPosts = Post.objects.filter(postAuthor=getUser).order_by('-postDate')

        friends = getProfile.friends.all()

        getNumberFriends = len(friends)

        if len(friends) == 0:
            is_friend = False

        for friend in friends:
            if friend == request.user:
                is_friend = True
                break
            else:
                is_friend = False

        return render(request, 'konto/userProfile.html', {
            'getProfile': getProfile,
            'getUser': getUser,
            'getPosts': getPosts,
            'getNumberFriends': getNumberFriends,
            'is_friend': is_friend,
            'friends': friends,
        })


@method_decorator(login_required, name='dispatch')
class UpdateProfileView(UpdateView):
    model = Profile
    template_name = 'konto/updateProfileUser.html'
    form = ProfileUpdateForm()
    fields = ['biography', 'profileAvatar', 'birthDate', 'currentLocation', 'countryOrigin']

    def get_success_url(self):
        return reverse_lazy('userProfile', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user == self.get_object().user


@method_decorator(login_required, name='dispatch')
class AddFriend(View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.friends.add(request.user)

        return redirect('userProfile', pk=profile.pk)


@method_decorator(login_required, name='dispatch')
class RemoveFriend(View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.friends.remove(request.user)

        return redirect('userProfile', pk=profile.pk)
