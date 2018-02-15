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

    def test_code_generator(self):
        '''
        Test the code generator method of the Urls class
        '''
        self.url.save()
        shortcode = self.url.code_generator()
        is_exitent = self.url.shortcode_exist('hrhje')
        self.assertEqual(is_exitent,True) 

    def test_get_url_by_shorcode(self):
        '''
        Tests the get_url_by shortcode method of the class Urls
        '''
        self.url.save()
        url = Urls.get_url_by_shorcode('hrhje')
        self.assertTrue(url.short_id == 'hrhje' )

class OtherFunctionsTestClass(TestCase):
    '''
    Test class that test the characteristics of other methods and 
    functionalities of the app
    '''
    
    def setUp(self):
        '''
        Method that runs at the beggining of each test
        '''
        self.url = Urls(short_id = 'hrhje', httpurl ='http://google.com')

    def test_Url_Validator(self):




        

    
