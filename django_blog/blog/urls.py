from django.urls import path
from . import views

from .views import PostSearchView
from .views import PostByTagListView



urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),

    # Blog CRUD
    path("posts/", views.PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/new/", views.PostCreateView.as_view(), name="post-create"),   
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),  
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
    
    
     # Comment URLs
    path("post/<int:pk>/comments/new/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/update/", views.CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
    
    
    path("profile/<int:pk>/", views.ProfileDetailView.as_view(), name="profile-detail"),
    path("profile/<int:pk>/edit/", views.ProfileUpdateView.as_view(), name="profile-update"),
    
    path("search/", PostSearchView.as_view(), name="post-search"),
    
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="posts-by-tag"),  # ✅ new




]
