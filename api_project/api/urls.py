from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

#  Create a router instance
router = DefaultRouter()

#  Register BookViewSet with the router
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    #  Include router URLs (CRUD endpoints for BookViewSet)
    path('', include(router.urls)),
]
