from django.shortcuts import render
from insurance.models import Branch

def home(request):
    return render(request, 'home.html')