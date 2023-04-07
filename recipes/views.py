from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'recipes/home.html',{
        'name':'Wesley'
    })


def contato(request):
    return HttpResponse('CONTATO')
    #HTTP response

def sobre(request):
    return HttpResponse('SOBRE')
    #HTTP response