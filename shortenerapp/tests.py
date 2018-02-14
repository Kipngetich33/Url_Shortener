from django.test import TestCase
from . models import Urls

class UrlsTestClass(TestCase):
    '''
    Class that test the characterics of the Urls objects and its methods
    '''
    def setUp(self):
        '''
        Method that runs at the beginning of each test
        '''
        self.url = Urls(short_id = 'hrhje', httpurl ='http://google.com')

    def test_isinstance(self):
        '''
        tets that detetmines whether an object is an instance of the class Urls
        '''
        self.assertTrue(isinstance(self.url,Urls))

    def test_save_url(self):
        '''
        test the Urls class save method
        '''
        self.url.save_url()
        saved_urls = Urls.objects.all()
        self.assertTrue(len(saved_urls)>0)

    def test_count_unique(self):
        '''
        Test count_unique method of the Urls class
        '''
        self.url.save()
        all = Urls.count_unique('http://google.com')
        self.assertTrue(all == 1)

    def test_code_generator(self):
        '''
        Test the code generator method of the Urls class
        '''
        self.url.save()
        shortcode = Urls.code_generator() 
        self.assertTrue(len(shortcode) == 6)

    def test_is_unique(test):
        '''
        Test the is unique
