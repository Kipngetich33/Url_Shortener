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
        prefix = 'http//:r/'
        httpurl = prefix

        count = Urls.objects.filter(httpurl = search_name).count()
        if count <= 0:
            message = 'inexistent'
        else:
            message = 'Exitent'
    else:
        message = 'No input'

    return render(request,'makeshort.html',{"message":message})

def s(request, httpurl):
    try:    
        is_saved = Urls.objects.get( httpurl = httpurl)
        short_url = is_saved.short_id
        message = 'Url already exists'
        return render(request,'makeshort.html',{"short_url":short_url, "message":message})
    except:
        message = 'Url already exists'
        return render(request,'statistics.html',{"httpurl":httpurl,"message":message})
