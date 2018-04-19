from django.shortcuts import render
from utils.utils import calculaMediaFinal
from django.http import HttpResponse

def media(resquest):
    media = calculaMediaFinal(10,8)
    return HttpResponse(media)

# Create your views here.
