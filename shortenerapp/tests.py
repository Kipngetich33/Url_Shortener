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
        shortcode = self.code_generator()
        self.assertTrue(len(shortcode) == 6)

    def test_shortcode_exist(self):
        '''
        Test the is is unique method of the Urls class
        '''
        self.url.save()
        is_exitent = Urls.shortcode_exist('hrhje')
        self.assertTrue(is_exitent == True)

    def test_url_exist(self):
        '''
        Method that tests url_exist method
        '''
        self.url.save()
        is_exitent = Urls.url_exist('http://google.com')
        self.assertTrue(is_exitent == True)


        

    
