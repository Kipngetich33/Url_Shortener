# APP NAME

### URL SHORTENER

## AUTHOR

Kipngetich Ngeno

## DESCRIPTION

This is an application that allows users to shortern their urls as well as keep track of the number of clicks that each URL gets

## User stories
As a user can do the following:
* Enter your url and generate a shorter url
* Keep track of the number of clicks that are made to a website
* Find all the available shortcodes as well as their original URLs

## Set Up and Installation

#### Prerequisites

* Python 3.6.2
* Virtual environment
* Postgres Database
* Reliable Internet Connection

## Installation Process

* Copy repolink

in your terminal run the following commands

* $ git clone REPO-URL in your terminal
* $ cd Url_Shortener
* $ python3.6 -m venv virtual
* $ touch .env ( to the file add :
        SECRET_KEY=<your secret key>
        DEBUG=True)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt
* $ psql ; CREATE DATABASE instagram ;

In the settings.py module of the project make the following changes

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shortner',
        'USER': *POSTGRES_USERNAME*,
        'PASSWORD': *POSTGRES_USERNAME*,
    }
}

* $ python3.6 manage.py runserver (this command runs the application of port http://127.0.0.1/8000 )
 
## Known Bugs

No known bugs

## CREDITS

Moringa School,Python Documentation, StackOverflow.com and W3 schools

## Technologies Used

This project uses major technologies which are :

* HTML5/CSS
* Bootstrap
* Python3.6
* Django Frane Work
* Postgress Database

## Support and Contacts

In case You have any issues using this code please do no hesitate to get in touch with me through khalifngeno@gmail.com or leave a commit here on github.

## License 

Copyright MIT [LiCENSE](./LICENSE) (c) 2017 [Kipngetich Ngeno](https://github.com/Kipngetich33)

