from django.shortcuts import render,redirect
from . models import code_generator, Urls
from . forms import UrlForm

def h(request):
    shortcode = code_generator(6,'1234567890afuhufxrkerwcklbvds')
    return render(request,'home.html',{"shortcode":shortcode})

def r(request):
    if 'name' in request.GET and request.GET["name"]: 
        search_name = request.GET.get("name")
        prefix = 'http//:r/'
        httpurl = prefix

        count = Urls.objects.filter(httpurl = search_name).count()
        if count <= 0:
            shortcode = code_generator(6,'1234567890afuhufxrkerwcklbvds')
            new_url = Urls (short_id = shortcode,httpurl = search_name )
            new_url.save()
            httpurl = search_name 
            message = 'short code created successfully'
        else:
            shortcode = Urls.objects.get(httpurl = search_name).short_id
            httpurl = Urls.objects.get(httpurl = search_name).httpurl
            message = 'A short url for the entered url already exists'
    else:
        shortcode ='You cannot create a shortcode with an empty input'
        message = 'You have not entered any url'
        httpurl = ''

    return render(request,'makeshort.html',{"message":message,"shortcode":shortcode, "httpurl":httpurl})

def s(request, httpurl): 
    httpurl = httpurl
    return redirect(f'{{httpurl}}')
