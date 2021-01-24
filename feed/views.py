from django.shortcuts import render
from django.views import View
from .models import Posts , Comments
from .forms import PostForm, CommentsForm
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

class PostsView(View):
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        post = Posts.objects.all().order_by('-creationDate')

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()

        context = {
            'allPosts': post,
            'form': form
        }
        return render(request, 'feed/posts.html', context)

    def get(self, request, *args, **kwargs):
        form = PostForm()
        post = Posts.objects.all().order_by('-creationDate')

        context = {
            'allPosts': post,
            'form': form
        }
        return render(request, 'feed/posts.html', context)


class PostsDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = Posts.objects.get(pk=pk)
        form = CommentsForm()

        comments = Comments.objects.filter(post=post).order_by('-creationDate')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }
        return render(request, 'feed/postsDetail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Posts.objects.get(pk=pk)
        form = CommentsForm(request.POST)

        if form.is_valid():
            newComment = form.save(commit=False)
            newComment.user = request.user
            newComment.post = post
            newComment.save()

        comments = Comments.objects.filter(post=post).order_by('-creationDate')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }
        return render(request, 'feed/postsDetail.html', context)







class PostsUpdateView(UpdateView):
    model = Posts
    fields = ['description']
    template_name = 'feed/postsUpdate.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('feed:detailPost', kwargs={'pk': pk})

class DeletePostsView(DeleteView):
    model = Posts
    template_name = 'feed/postsDelete.html'
    success_url = reverse_lazy('feed:allPosts')



