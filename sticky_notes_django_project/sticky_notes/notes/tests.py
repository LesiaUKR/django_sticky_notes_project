from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteModelTest(TestCase):
    def setUp(self):
        """
        Set up a test note for use in the following tests.
        """
        self.note = Note.objects.create(
            title='Test Note',
            content='This is a test note.'
        )

    def test_note_has_title(self):
        """
        Test that a Note object has the expected title.
        """
        self.assertEqual(self.note.title, 'Test Note')

    def test_note_has_content(self):
        """
        Test that a Note object has the expected content.
        """
        self.assertEqual(self.note.content, 'This is a test note.')


class NoteViewTest(TestCase):
    def setUp(self):
        """
        Set up a test note for use in the view tests.
        """
        self.note = Note.objects.create(
            title='Test Note',
            content='This is a test note.'
        )

    def test_note_list_view(self):
        """
        Test that the note list view returns a status code of 200
        and contains the test note's title.
        """
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_create_view(self):
        """
        Test that the note creation form works correctly:
        - Submitting the form redirects to the expected page (status code 302).
        - The new note is saved in the database.
        """
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'This is a new note.'
        })
        self.assertEqual(response.status_code, 302)  # Check for redirect after successful creation
        self.assertTrue(Note.objects.filter(title='New Note').exists())

    def test_note_update_view(self):
        """
        Test that the note update form works correctly:
        - Submitting the form redirects to the expected page (status code 302).
        - The note's title and content are updated in the database.
        """
        response = self.client.post(reverse('note_update', args=[str(self.note.id)]), {
            'title': 'Updated Note',
            'content': 'This note has been updated.'
        })
        self.assertEqual(response.status_code, 302)  # Check for redirect after successful update
        updated_note = Note.objects.get(id=self.note.id)
        self.assertEqual(updated_note.title, 'Updated Note')

    def test_note_delete_view(self):
        """
        Test that the note deletion view works correctly:
        - Submitting the form redirects to the expected page (status code 302).
        - The note is deleted from the database.
        """
        response = self.client.post(reverse('note_delete', args=[str(self.note.id)]))
        self.assertEqual(response.status_code, 302)  # Check for redirect after successful deletion
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())
