
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from main.models import library

class LibraryViewTest(APITestCase):

    def setUp(self):
        """Set up test users and books."""
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")

        self.book = library.objects.create(
            title="Flask Testing",
            author="Miguel Grinberg",
            published_date="2023-05-15",
            added_by=self.user
        )

    def test_list_books(self):
        """Test listing all books."""
        url = reverse("library")  # Ensure the name matches your URL pattern
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)  # Ensure at least one book exists

    def test_create_book(self):
        """Test adding a new book."""
        url = reverse("library")
        data = {
            "title": "New Django Book",
            "author": "Alice",
            "published_date": "2024-01-10",
            "added_by": self.user.id
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(library.objects.count(), 2)

    def test_retrieve_book(self):
        """Test retrieving a single book by ID."""
        url = reverse("library/<int:pk>", args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Django Testing")

    def test_update_book(self):
        """Test updating a book."""
        url = reverse("library/<int:pk>", args=[self.book.id])
        data = {"title": "Updated Django Book"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Django Book")

    def test_delete_book(self):
        """Test deleting a book."""
        url = reverse("library/<int:pk>", args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(library.objects.count(), 0)


class BorrowReturnBookTest(APITestCase):

    def setUp(self):
        """Set up test users and books."""
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")

        self.book = library.objects.create(
            title="Django for Professionals",
            author="Michael Herman",
            published_date="2023-06-01",
            added_by=self.user
        )

    def test_borrow_book(self):
        """Test borrowing a book."""
        url = reverse("book", args=[self.book.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.borrowed_by, self.user)

    def test_return_book(self):
        """Test returning a borrowed book."""
        # First, borrow the book
        self.book.borrowed_by = self.user
        self.book.save()

        url = reverse("return", args=[self.book.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertIsNone(self.book.borrowed_by)
