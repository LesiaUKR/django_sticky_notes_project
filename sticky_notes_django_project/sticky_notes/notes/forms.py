from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """Form for the Note model.

    This form is used for creating and editing notes.

    Attributes:
        model (Note): The model associated with this form.
        fields (list): The fields to be included in the form.
    """
    class Meta:
        model = Note
        fields = ['title', 'content']
