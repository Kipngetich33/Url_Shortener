from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.h,name = 'home'), 
    url(r'^s/(?P<shortcode>[-_\w.]+)',views.s, name = 'statistics'),
    url(r'^r/',views.r, name = 'makeshort'),
    url(r'^l/',views.l, name = 'last'),
    url(r'^a',views.a, name = 'all'), 
    url(r'^w',views.w, name = 'wrong'), 
    url(r'^t',views.t, name = 'test'),
    url(r'^t2',views.t2, name = 'test2'), 
]