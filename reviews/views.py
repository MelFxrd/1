from django.shortcuts import render
from .models import Review

def home_page(request):
    reviews = Review.objects.all()
    return render(request, 'home.html', {'reviews': reviews})