from django.test import TestCase
from django.contrib.auth.models import User
from main.models import library
from django.utils.timezone import now

class LibraryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.lib =library.objects.create(
            title="Programming in GO",
            author="Mark Summerfield",
            published_date="2022-01-01",
            added_by=self.user
        )

    def test_book_creation(self):
        """Test if the book instance is created correctly."""
        self.assertEqual(self.lib.title, "Programming in GO")
        self.assertEqual(self.lib.author, "Mark Summerfield")
        self.assertEqual(self.lib.added_by, self.user)

    def test_book_string_representation(self):
        """Test the book's string representation."""
        self.assertEqual(str(self.lib), "Programming in GO")    

