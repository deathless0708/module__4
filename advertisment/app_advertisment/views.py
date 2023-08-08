from django.shortcuts import render
from django.http import HttpResponse as hp


# Create your views here.

def index(request):
    return render(request, 'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')

# def start(request):
#     return hp('hpfgjhfgjhodphjhhjpijdprthjrtid')