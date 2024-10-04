from django.shortcuts import render
from .models import JobListing

def home_view(request):
    jobs = JobListing.objects.all()  # Fetch all job listings
    return render(request, 'home.html', {'jobs': jobs})
