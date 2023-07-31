from django.shortcuts import render
from django.http import HttpResponse as hp


# Create your views here.
def index(request):
    return hp('Это мой первый сайт!(Хотя получается неа)')

def start(request):
    return hp('hpfgjhfgjhodphjhhjpijdprthjrtid')