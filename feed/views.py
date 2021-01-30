from django.shortcuts import render
from django.views import View
from .models import Post, Comment
from .forms import PostCreateForm, CommentCreateForm
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect


@method_decorator(login_required, name='dispatch')
class AllPostView(View):
    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST)
        allPosts = Post.objects.all().order_by('-postDate')

        if form.is_valid():
            newPost = form.save(commit=False)
            newPost.postAuthor = request.user
            newPost.save()
            return HttpResponseRedirect(reverse_lazy('feed:all-posts'))

        return render(request, 'feed/allPost.html', {
            'allPosts': allPosts,
            'form': form
        })

    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        allPosts = Post.objects.all().order_by('-postDate')

        return render(request, 'feed/allPost.html', {
            'allPosts': allPosts,
            'form': form
        })


@method_decorator(login_required, name='dispatch')
class DetailPostView(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentCreateForm()

        allComments = Comment.objects.filter(post=post).order_by('-commentDate')

        return render(request, 'feed/detailPost.html', {
            'post': post,
            'form': form,
            'comments': allComments,
        })

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentCreateForm(request.POST)

        if form.is_valid():
            newComment = form.save(commit=False)
            newComment.commentAuthor = request.user
            newComment.post = post
            newComment.save()

        allComments = Comment.objects.filter(post=post).order_by('-commentDate')

        return render(request, 'feed/detailPost.html', {
            'post': post,
            'form': form,
            'comments': allComments,
        })


@method_decorator(login_required, name='dispatch')
class UpdatePostView(UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'feed/updatePost.html'
    fields = ['postContent']

    def test_func(self):
        return self.request.user == self.get_object().postAuthor

    def get_success_url(self):
        return reverse_lazy('feed:detail-post', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class DeletePostView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'feed/deletePost.html'
    success_url = reverse_lazy('feed:all-posts')

    def test_func(self):
        return self.request.user == self.get_object().postAuthor


@method_decorator(login_required, name='dispatch')
class DeleteCommentView(UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'feed/deleteComment.html'

    def test_func(self):
        return self.request.user == self.get_object().commentAuthor

    def get_success_url(self):
        return reverse_lazy('feed:detail-post', kwargs={'pk': self.kwargs['postPK']})
