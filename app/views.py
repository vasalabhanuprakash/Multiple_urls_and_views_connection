from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Fun1(request):
    return HttpResponse('<h1> This is my 1st view which is connectig to the url</h1>')


