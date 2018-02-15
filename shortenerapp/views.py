from django.shortcuts import render,redirect
from . models import Urls
from . forms import UrlForm
from django.http import HttpResponse, HttpResponseRedirect

def h(request):
    shortcode = Urls.code_generator()
    return render(request,'home.html',{"shortcode":shortcode})

def r(request):
    if 'name' in request.GET and request.GET["name"]: 
        search_name = request.GET.get("name")
        prefix = 'http//:r/'
        httpurl = prefix

        is_exist = Urls.url_exist(search_name)
        if is_exist == False:
            shortcode = Urls.code_generator()
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
        httpurl = 'empty'

    return render(request,'makeshort.html',{"message":message,"shortcode":shortcode, "httpurl":httpurl})

def s(request, shortcode): 
    try:
        is_shortcode = Urls.shortcode_exist(shortcode)
        if is_shortcode == True:
            requested_url = Urls.get_url_by_shorcode(shortcode)
            return redirect(requested_url.httpurl)
        else:
            return redirect(l)
    except:
        return redirect(w)

def l(request):
    message = ''
    return render(request, 'last.html',{"message":message})

def a(request):
    urls = Urls.objects.all()
    return render(request,'all.html',{"urls":urls})

def w(request):
    return render(request,'wrong.html')
