from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kohli(request):
    return HttpResponse('<i>KOHLI IS A GOOD PLAYER</i>')