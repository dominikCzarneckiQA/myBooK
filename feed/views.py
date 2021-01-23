from django.shortcuts import render
from django.views import View
from .models import Posts
from .forms import PostForm, CommentsForm


class postsView(View):
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        posts = Posts.objects.all().order_by('-creationDate')

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()

        context = {
            'allPosts': posts,
            'form': form
        }
        return render(request, 'feed/posts.html', context)

    def get(self, request, *args, **kwargs):
        form = PostForm()
        posts = Posts.objects.all().order_by('-creationDate')

        context = {
            'allPosts': posts,
            'form': form
        }
        return render(request, 'feed/posts.html', context)

class postsDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        posts = Posts.objects.get(pk=pk)
        form = CommentsForm

        context = {
            'post': posts,
            'form': form,
        }
        return render(request,'feed/postsDetail.html', context)
