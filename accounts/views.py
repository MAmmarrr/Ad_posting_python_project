from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'home.html')

def details(request,id):
    print(id)    
    return render(request, 'ad-details.html')
    