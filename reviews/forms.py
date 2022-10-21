from socket import fromshare
from .models import Review
from django import forms 

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'movie_name', 'image', 'grade']