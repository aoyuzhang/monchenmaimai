from django.shortcuts import render
from .models import Company

# Create your views here.

from django.http import HttpResponse

def home(request):
    companies = Company.objects.all()
    return render(request, "home.html", {"companies":companies})