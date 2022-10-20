from django.urls import path
from .views import(
    PostListView,
    UserPostListView,
    PostDetailView,
    PostCreateView,
    PostUpadateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    # path('user/<str:username>', UserPostListView.as_view(), name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('', PostCreateView.as_view(), name='post-create'),
    path('', PostUpadateView.as_view(), name='post-update'),
    path('', PostDeleteView.as_view(), name='post-delete'),
]
