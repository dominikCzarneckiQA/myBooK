from django.shortcuts import render
from django.views import View
from .models import Post
from .forms import postForm
class PostView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-data')
        form = postForm()
        context = {
            'postList': posts,
            'form': form
        }
        return render(request, 'feed/Posty.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-data')
        form = postForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'postList': posts,
            'form': form
        }
        return render(request, 'feed/Posty.html', context)