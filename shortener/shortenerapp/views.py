from django.shortcuts import render
from . models import code_generator

def home(request):
    shortcode = code_generator(6,'1234567890afuhufxrkerwcklbvds')
    return render(request,'home.html',{"shortcode":shortcode})

def makeshort(request,shortcode):
    return render(request,'makeshort.html',{"shortcode":shortcode})

def statistics(request):
    return render(request,'statistics.html')
