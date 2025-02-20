from django.db import models


class Note(models.Model):
    """Represents a note with a title, content, and timestamps.

    This model stores a note with a title and content, along with
    timestamps indicating when it was created and last updated.

    Attributes:
        title (CharField): The title of the note, limited to 100 characters.
        content (TextField): The main content of the note.
        created_at (DateTimeField): The timestamp when the note was created.
        updated_at (DateTimeField): The timestamp when the note was last updated.
    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns a string representation of the note, using its title."""
        return self.title
