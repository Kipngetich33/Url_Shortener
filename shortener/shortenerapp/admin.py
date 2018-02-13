from django.contrib import admin
from shortenerapp.models import Urls

class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id','httpurl','pu')
