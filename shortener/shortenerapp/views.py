from django.shortcuts import render,redirect
from . models import code_generator, Urls
from . forms import UrlForm

def h(request):
    shortcode = code_generator(6,'1234567890afuhufxrkerwcklbvds')
    return render(request,'home.html',{"shortcode":shortcode})

def r(request):
    if 'name' in request.GET and request.GET["name"]: 
        search_name = request.GET.get("name")
        shortcode = code_generator(6,'1234567890afuhufxrkerwcklbvds')
        prefix = 'http//:'
        short_url = prefix + shortcode

        return render(request,'makeshort.html',{"short_url":short_url})
    return render(request,'makeshort.html')

def s(request):
    return render(request,'statistics.html')
