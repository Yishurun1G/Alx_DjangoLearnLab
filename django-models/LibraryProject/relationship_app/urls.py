from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, register

urlpatterns = [
    # Book & Library URLs
    path("books/", list_books, name="list_books"),  # Function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # Class-based view

    # User Authentication URLs (checker expects class-based for login/logout)
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", register, name="register"),  # Function-based registration
]
