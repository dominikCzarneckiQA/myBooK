# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView, DeleteView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from feed.models import Post

from .forms import LoginForm, UserRegisterForm, UserEditForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.models import User

from django.contrib.auth.mixins import UserPassesTestMixin


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
                messages.warning(request, 'Nieprawidłowe dane! Spróbuj ponownie.')
                return HttpResponse("Nieprawidłowe dane! Spróbuj ponownie. ")
    else:
        form = LoginForm()
    return render(request, 'konto/login.html', {'formularz': form})


#  widok rejestracyjny nowych użytkowników

def registerView(request):
    if request.method == 'POST':
        userForm = UserRegisterForm(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Ten adres jest już używany przez innego użytkownika')
            return redirect('register')
        else:
            if userForm.is_valid():
                newUser = userForm.save(commit=False)
                newUser.set_password(
                    userForm.cleaned_data['password1'])
                messages.success(request, 'Rejestracja zakończyła się pomyślnie')
                newUser.save()
                Profile.objects.create(user=newUser)

                return render(request, 'konto/register_success.html',
                              {'nowy_uzytkownik': newUser})
    else:
        messages.warning(request, 'Coś poszło nie tak..')
        userForm = UserRegisterForm()
    return render(request, 'konto/register.html',
                  {'user_form': userForm})


@login_required()
def editView(request):
    if request.method == 'POST':
        userForm = UserEditForm(instance=request.user, data=request.POST)
        if userForm.is_valid():
            messages.success(request, 'Edycja przebiegła pomyślnie')
            userForm.save()

    else:
        userForm = UserEditForm(instance=request.user)

    return render(request, 'konto/userUpdate.html',
                  {
                      'userForm': userForm,
                  })


@method_decorator(login_required, name='dispatch')
class UserProfileView(View):
    @staticmethod
    def get(request, pk, *args, **kwargs):

        global is_follower
        getProfile = Profile.objects.get(pk=pk)
        getUser = getProfile.user
        getPosts = Post.objects.filter(postAuthor=getUser).order_by('-postDate')

        followersList = getProfile.followers.all()

        if len(followersList) == 0:
            is_follower = False

        for follower in followersList:
            if follower == request.user:
                is_follower = True
                break
            else:
                is_follower = False

        getNumberFollowers = len(followersList)

        return render(request, 'konto/userProfile.html', {
            'is_follower': is_follower,
            'getProfile': getProfile,
            'getUser': getUser,
            'getPosts': getPosts,
            'getNumberFollowers': getNumberFollowers,
            'followersList': followersList,

        })


@method_decorator(login_required, name='dispatch')
class UpdateProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    updateform = ProfileUpdateForm
    template_name = 'konto/userProfileUpdate.html'

    fields = ['biography', 'profileAvatar', 'birthDate', 'city', 'countryOrigin', 'github', 'snapchat',
              'instagram', 'facebook', 'twitter']

    def get_success_url(self):
        return reverse_lazy('userProfile', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user == self.get_object().user




@method_decorator(login_required, name='dispatch')
class UserFollow(View):
    @staticmethod
    def post(request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.add(request.user)

        return redirect('userProfile', pk=profile.pk)


@method_decorator(login_required, name='dispatch')
class UserUnfollow(View):
    @staticmethod
    def post(request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.remove(request.user)

        return redirect('userProfile', pk=profile.pk)


@method_decorator(login_required, name='dispatch')
class UsersListView(View):
    template_name = 'konto/userList.html'

    def get(self, request):
        users = User.objects.all()
        return render(request, self.template_name,
                      {
                          'users': users,
                      })


class UserSearchView(View):
    def get(self, request, *args, **kwargs):
        getQuest = self.request.GET.get('quest')
        getProfileList = Profile.objects.filter(
            Q(user__username__icontains=getQuest, followers__first_name__isnull=False)
        )

        return render(request, 'konto/userSearch.html',
                      {
                          'getProfileList': getProfileList,
                      })
