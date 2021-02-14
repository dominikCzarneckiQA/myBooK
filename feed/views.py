from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post, Comment
from .forms import PostCreateForm, CommentCreateForm
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from konto.models import Profile


@method_decorator(login_required, name='dispatch')
class AllPostView(View):
    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST)
        allPosts = Post.objects.all().order_by('-postDate')

        if form.is_valid():
            newPost = form.save(commit=False)
            newPost.postAuthor = request.user
            newPost.save()
            form.save()

            return HttpResponseRedirect(reverse_lazy('feed:all-posts'))

        return render(request, 'feed/allPost.html', {
            'allPosts': allPosts,
            'form': form,

        })

    def get(self, request, *args, **kwargs):
        formAllPost = PostCreateForm()
        allPosts = Post.objects.all().order_by('-postDate')
        allUsers = Profile.objects.all()

        return render(request, 'feed/allPost.html', {
            'allPosts': allPosts,
            'form': formAllPost,
            'allUsers': allUsers,
        })


@method_decorator(login_required, name='dispatch')
class DetailPostView(View):

    def get(self, request, pk, *args, **kwargs):
        postget = Post.objects.get(pk=pk)
        formDetail = CommentCreateForm()

        allComments = Comment.objects.filter(post=postget).order_by('-commentDate')
        something = get_object_or_404(Post, id=self.kwargs['pk'])
        ifLiked = False

        if something.postLikes.filter(id=self.request.user.id).exists():
            ifLiked = True

        return render(request, 'feed/detailPost.html', {
            'post': postget,
            'form': formDetail,
            'comments': allComments,
            'something': something,
            'ifLiked': ifLiked,
        })

    def post(self, request, pk, *args, **kwargs):
        postget = Post.objects.get(pk=pk)
        formDetail = CommentCreateForm(request.POST)

        if formDetail.is_valid():
            newComment = formDetail.save(commit=False)
            newComment.commentAuthor = request.user
            newComment.post = postget
            newComment.save()

        allComments = Comment.objects.filter(post=postget).order_by('-commentDate')

        return render(request, 'feed/detailPost.html', {
            'post': postget,
            'form': formDetail,
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


# UserPassesTestMixin
@method_decorator(login_required, name='dispatch')
class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'feed/deleteComment.html'

    # def test_func(self):
    #    return self.request.user == self.get_object().commentAuthor

    def get_success_url(self):
        return reverse_lazy('feed:detail-post', kwargs={'pk': self.kwargs['post_pk']})


def LikePostDetailView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post.pk'))

    ifLiked = False
    if post.postLikes.filter(id=request.user.id).exists():
        post.postLikes.remove(request.user)
        ifLiked = False
    else:
        post.postLikes.add(request.user)
        ifLiked = True
    return HttpResponseRedirect(reverse_lazy('feed:detail-post', args=[str(pk)]))
