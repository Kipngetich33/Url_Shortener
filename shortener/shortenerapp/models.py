from django.db import models
import random


def code_generator(size , char ):
    new_code = ''
    for i in range(size):
        new_code += random.choice(char)
    return new_code

new_code = code_generator(6, '1234567890afuhufxrkerwcklbvds')
print(new_code) 

 
# Create your models here.
class Urls(models.Model):
    short_id = models.SlugField(max_length=6,primary_key=True)
    httpurl = models.URLField(max_length=200, null = True)
    pub_date = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)
 
def __str__(self):
    return self.httpurl
