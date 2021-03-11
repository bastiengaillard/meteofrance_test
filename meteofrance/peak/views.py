from django.shortcuts import render
import requests
from .models import Peak

def index(request):
    response = requests.get('http://localhost:8000/peak/api')
    peaks = response.json()
    return render(request, 'peak/index.html', { 'peaks' : peaks })

