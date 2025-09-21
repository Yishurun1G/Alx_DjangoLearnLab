from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from .models import Book
from .forms import ExampleForm, BookForm

# ExampleForm view (for the checker)
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book created successfully!")
            return redirect('book_list')  # replace with your book list URL name
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

# List all books (viewable by anyone)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Create a book (requires can_create permission)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book created successfully!")
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/create_book.html', {'form': form})

# Edit a book (requires can_edit permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully!")
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form})

# Delete a book (requires can_delete permission)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted successfully!")
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})
