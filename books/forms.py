from django import forms
from .models import Book, Review


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'description', 'price', 'cover']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'author', 'text',]