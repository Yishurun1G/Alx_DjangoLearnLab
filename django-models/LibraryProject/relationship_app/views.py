from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

# Admin-only view
@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

# Librarian-only view
@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

# Member-only view
@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Member')
def member_view(request):
    return render(request, "relationship_app/member_view.html")
