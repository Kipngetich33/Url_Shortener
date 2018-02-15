from django.test import TestCase
from . models import Urls, Statistics

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

    def test_get_shortcode_by_url(self):
        '''
        Tests the get_shortcode_by_url method of the Urls class
        '''
        self.url.save()
        requested_url = Urls.get_shortcode_by_url('http://google.com')
        self.assertTrue(requested_url.short_id == 'hrhje')

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
        pass

class StatisticsTestClass(TestCase):
    '''
    Tests the characteristics of the statistics class
    '''
    def setUp(self):
        '''
        Method that runs at the begining of each test
        '''
        self.statistic = Statistics(name='statistics')

    def test_isinstance(self):
        '''
        Method that test if an object is an instance of a given Class
        '''
        self.assertTrue(isinstance(self.statistic,Statistics))

    def test_get_total_clicks(self):
        '''
        Method that test get_total_clicks method
        '''
        self.statistic.save()
        self.statistic.total_clicks +=1
        self.statistic.save()
        self.assertTrue(Statistics.get_total_clicks() == 1)

    def test_calculate_popularity(self):
        '''
        Method that test the calculate_popularity method
        '''
        self.statistic.save()
        self.statistic.total_clicks +=2
        calculated_index = Statistics.calculate_popularity(1)
        self.statistic.save()
        self.assertTrue(calculated_index == 2)




    




        

    
