from django.shortcuts import render,redirect
from . models import Urls
from . forms import UrlForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def h(request):
    if request.method == 'POST':

        form = UrlForm(request.POST)

        if form.is_valid():
            search_name = form.cleaned_data['entered_url']
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
            return render(request,'makeshort.html',{"message":message,"shortcode":shortcode, "httpurl":httpurl})
    else:
        form = UrlForm()
    return render(request,'home.html',{"form":form})


def r(request):
    if search_name:
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

def t(request):
    '''
    this is a general test view function that enables me to test the various aspects 
    of the app before applying changes to an intended view function
    '''
    form = UrlForm()
    if request.method == 'POST':

        form = UrlForm(request.POST)

        if form.is_valid():
            search_name = form.cleaned_data['entered_url']
            
            return render(request,'test2.html',{"message":search_name,"form":form})
    else:
        form = UrlForm()
    return render(request,'test.html',{"form":form})

def t2(request):
    return render(request,'test2.html',{"message":message})