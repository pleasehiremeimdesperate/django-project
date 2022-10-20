from urllib import request
from django.shortcuts import get_object_or_404, render
from django.views.generic import (DeleteView, ListView, DetailView,
                                 CreateView, UpdateView)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(ListView):
    model = Post
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model= Post

class UserPostListView(ListView):
    model = Post

    def get_queryset(self):
        username = get_object_or_404(User, user=self.kwargs.get('username'))
        return Post.objects.filter(author=username).order_by('-date_posted')
    
class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpadateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    Model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            True
        else:
            False

class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post

    def test_func(self):
        post = self.get_object()
    
        if self.request.user == post.author:
            return True
        False
        