from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def note_list(request):
    """Retrieves and displays all notes.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered template displaying all notes.
    """
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})


def note_create(request):
    """Handles the creation of a new note.

    If the request method is POST, the form is validated and saved.
    Otherwise, an empty form is displayed.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Redirects to the note list on success,
        or re-renders the form if invalid.
    """
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})


def note_update(request, pk):
    """Handles updating an existing note.

    If the request method is POST, the form is validated and saved.
    Otherwise, the existing note's details are pre-filled in the form.

    Args:
        request (HttpRequest): The request object.
        pk (int): The primary key of the note to update.

    Returns:
        HttpResponse: Redirects to the note list on success,
        or re-renders the form if invalid.
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})


def note_delete(request, pk):
    """Handles deleting a note.

    If the request method is POST, the note is deleted and the user is
    redirected.

    Args:
        request (HttpRequest): The request object.
        pk (int): The primary key of the note to delete.

    Returns:
        HttpResponse: Redirects to the note list after deletion,
        or displays a confirmation page.
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})
