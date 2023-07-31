from django.shortcuts import render
from django.http import HttpResponse as hp

# Create your views here.

def index(request):
    return hp('Прииветик)) Домашка по 4 занятию. Хорошего вам дня <3')