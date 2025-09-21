from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # import the entire views module

urlpatterns = [
    # Book & Library URLs
    path("books/", views.list_books, name="list_books"),  # Function-based view
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),  # Class-based view

    # User Authentication URLs
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),  # Function-based registration
]
