from django.db import models
import random


# Create your models here.
class Urls(models.Model):
    short_id = models.SlugField(max_length=6,primary_key=True)
    httpurl = models.URLField(max_length=200, null = True)
    pub_date = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)
 
    def __str__(self):
        return self.httpurl

    def save_url(self):
        '''
        Method that saves Urls objects
        '''
        self.save()

    @classmethod
    def count_unique(cls,httpurl):
        '''
        Method that counts the number of object with a given httpurl in the database
        '''
        all = cls.objects.filter(httpurl = httpurl).count()
        return all

    @classmethod
    def shortcode_exist(cls,short_id):
        '''
        Method that determines whether a provided short_id exists in the database
        '''
        is_exitent = cls.objects.filter(short_id = short_id).count()
        if is_exitent > 0:
            return True
        else:
            return False

    @classmethod
    def url_exist(cls,httpurl):
        '''
        Method that determines whether a provided httpurl exists in the database
        '''
        is_exitent = cls.objects.filter(httpurl = httpurl).count()
        if is_exitent > 0:
            return True
        else:
            return False

    @classmethod
    def code_generator(cls,size = 6 , char = '1234567890afuhufxrkerwcklbvds' ):
        '''
        Method that creates a unique shortcode for each given httpurl
        '''
        new_code = ''
        for i in range(size):
            new_code += random.choice(char)
        is_exitent = cls.shortcode_exist(new_code)
        if is_exitent == True:
            cls.code_generator()
        else:
            return new_code
    
    @classmethod
    def get_url_by_shorcode(cls,short_id):
        '''
        Method that fetches a url object attached to the provided short_id
        '''
        url = cls.objects.get(short_id= short_id)
        return url


    
