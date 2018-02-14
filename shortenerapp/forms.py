from django import forms

class UrlForm(forms.Form):
    '''
    class that creates the url submit form
    ''' 
    entered_url = forms.CharField(label='Enter Url',max_length = 300)