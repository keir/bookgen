from django.shortcuts import render
import random
from generation.models import *

def home(request):
    
    book = Book.objects.order_by('?').first()
    genre = book.genre
    
    font = Font.objects.filter(genre=genre).order_by('?').first().name
    
    return render(request, 'generation/home.html', {'book': book, 'font': font})