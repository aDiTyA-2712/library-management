from django.shortcuts import render
from .models import library
from .serializers import librarySerializer
from rest_framework import generics,permissions,filters
from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import PermissionDenied
# Create your views here.

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils.timezone import now
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

class LibraryListCreateView(generics.ListCreateAPIView):
    queryset=library.objects.all()
    serializer_class=librarySerializer
    permission_classes=[permissions.IsAuthenticated]
    filter_backends=[filters.SearchFilter,DjangoFilterBackend]
    search_fields=['title','author']

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)  # assign to logged in user


class LibraryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=library.objects.all()
    serializer_class=librarySerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.get_object().added_by!=self.request.user:
            raise PermissionDenied("Cannot update as you are not authorized to do it.")
        serializer.save()

    def perform_desstroy(self, instance):
        if instance.added_by!=self.request.user:
            raise PermissionDenied("Cannot delete as you are not authorized to do it.")
        instance.delete()    


@login_required
def borrow(request,pk):     
    book=get_object_or_404(library,uid=pk)

    if book.is_borrowed:
        return JsonResponse({"error":"already borrowed"},status=200)
    

    book.is_borrowed = True
    book.borrowed_by = request.user
    book.borrowed_at = now()
    book.save()

    send_mail(
        "Book Borrowed",
        f"You have borrowed the book: {book.title}",
        "admin@library.com",
        [request.user.email],
        fail_silently=True,
    )

    return JsonResponse({"message":f"borrowed - {book.title}"})

@login_required
def book_return(request,pk):
    book=get_object_or_404(library,uid=pk)

    if not book.is_borrowed or book.borrowed_by != request.user:
        return JsonResponse({"error": "You cannot return this book!"}, status=400)
    
    book.is_borrowed = False
    book.borrowed_by = None
    book.borrowed_at = None
    book.save()

    send_mail(
        "Book Returned",
        f"You have returned the book: {book.title}",
        "admin@library.com",
        [request.user.email],
        fail_silently=True,
    )

    return JsonResponse({"message": f"You have returned {book.title}"})
