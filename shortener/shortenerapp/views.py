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

        try:
            is_saved = Urls.objects.get( httpurl = search_name)
            short_url = prefix+is_saved.short_id
            message = 'Url already exists'
            return render(request,'makeshort.html',{"short_url":short_url, "message":message})
        except:
            short_url = prefix + shortcode
            new_id = Urls(short_id = shortcode,httpurl = search_name)
            new_id.count +=1
            new_id.save()
            message = 'Short Url Created successfully'
            return render(request,'makeshort.html',{"short_url":short_url, "message":message})

def s(request):
    return render(request,'statistics.html')
