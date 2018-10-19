[![Build Status](https://travis-ci.org/solomonj2k12/Web_Store.svg?branch=master)](https://travis-ci.org/solomonj2k12/Web_Store)

# Web Store

The purpose of this application did change over the course of the development process, at the start i planned for the website to aid new web developers by providing a forum where they could express their issues to other developers and help each other, also offer a premium service where i would help them out, with any advance issues or creation of functionality. However i adapted and worked on this idea to create a web application where i offer a store, which has many different services which link to web development, the purpose was to help to kind of people and they were other web developers who might be struggling in creating certain things for their web application and to help people who don't want to go through the whole process of learning how to code and create a web application but rather pay and work with somebody else to get what they want. For both of these kind of people i offer my services.

As the website grew i would take on other people like me to help with completing tasks bought buy customers and then eventually create a web page bit like ebay where users could add their own products and services to help others and i would take a cut from this or customers could go straight to us for help.

## UX

As mentioned before the web purpose did change over the development process so the mockups which were first made are not made for the correct website but i did use and then i adapted/worked on them. They can be found in the mockups folder in the repo

1. The first main thing for the webpage was a SignUp/SignIn feature, so that users could create an account to gain access to the main features of the site but also to have identity to the website, so i could identify them through the admin page.

2. Next was the store, where i would advertise my products to the users, so that i could provide enough information to the user so they know what service to choose for their issue and good advertising will lead to more sales.

3. After this was of course was adding a cart feature, so that users could add products to the cart to get a overview of what they are buying and the cost of buying selected products, also to use the cart to remove any unwanted products or to add extra products.

4. With a cart you need a checkout feature, so that the user can buy the items and enter their personal details correctly for the payment to go through, so that i could then start working on what they have bought.

5. To aid with the store i added a search bar, so when eventually there will be many products the search bar will filter the items in the store to help the user to find what they want.

6. Finally there is a post feature, where customer can post reviews on the service, so other users can get idea of how good my services are.

7. Also to aid in the purpose of the website there is some sort of about on the home page of the site to aid in teaching new users on how the website works

8. Its a more of a work in progress but a simple profile page so the user can see what their email is for the site

### Features

1. SignUp/SignIn forms for user registration

2. user logout function

3. Forgot password function/ send real emails through gmail accounts

4. Nav bar with mobile first design

5. ability to add products to cart, adjust number of products in cart and remove products in cart

6. complete checkout feature with stripe integration

7. messages for logging in, logging out, products purchase and so on

8. profile page

9. service review form with tags 

10. user admin page to view orders, users and add new products

#### Feature i would like to add

1. more advance profile page

2. individual pages for each product so i can add more information in description and give a better overview

3. profile id on reviews

##### Technologies Used

*Django
- The website is a Django project made up of 6 Django apps
- For handling user accounts and authentication
- For handling/storing products in store
- For handling the cart and checkouts
- For handling the search filter in the store
- For binding functions to URLs
- To unit test functions
- For modelling data
- To render HTML templates and include Python programming within these templates.
- To trigger functions on GET or POST requests

*Python3
- All apps are predominantly written using Python, the language of Django
- To create a Procfile to deploy the app on Heroku
- The website apps use imported Python libraries, including datetime and so on

*HTML , CSS and font-awesome
- To structure and style the web app content

*SQLite
- Used as the application database

*Bootstrap
- Used in with HTML and CSS to develop the website style
- Bootstrap components used includes panels, tables, and the navbar
- Bootstrap forms

*Stripe
- For processing credit card payments
- Stripe JavaScript file manages payment modal and verifying payments, ensuring that sensitive information is never posted on the app’s forms

*Amazon S3
- For storing and reading static files. This includes CSS, JavaScript, Django admin and Font-Awesome
- For storing and reading media files, such as images for products

*Travis CI
- For continuous testing. 

*Heroku
- The live version of the web app is hosted on Heroku:
https://web-store-sol.herokuapp.com/
- For saving configuration variables that should remain hidden from GitHub. This includes secret keys for Amazon AWS and Stripe


###### Deployment

Run Locally 
1.	Clone or download this GitHub repository using the ‘Clone or Download’ button found on the main page, then unzip file, if you want you can take       certain function by them self for your purpose but you will need to change certain dependencies in the setting.py file

2.	Open the project directory using an integrated development environment (IDE) software application, such as Cloud 9

3.	Next you will need to install all these packages 
- sudo pip3 install django
- sudo pip3 install django_forms_bootstrap
- sudo pip3 install pillow
- sudo pip3 install django-storages
- sudo pip3 install stripe

4. Because things such as the key are hidden, you will need to create your own so first add a env.py file on the top level, in this include:

"import os

os.environ.setdefault("STRIPE_PUBLISHABLE", "<key here>")
os.environ.setdefault("STRIPE_SECRET", "<key here>")
os.environ.setdefault("SECRET_KEY", "<key here>")
os.environ.setdefault("AWS_ACCESS_KEY_ID", "<key here>")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "<key here>")"

5. From here you will need to fill the keys in with your keys, these include:

*SECRET_KEY
- The project secret key

*AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID
- Required to post to the S3 bucket
- These are unique to the S3 bucket used on this project. If you wish to post data to S3 (e.g. new product images or JavaScript files), then you will   need to use your own S3 bucket
- you will need to do "python3 manage.py collectstatic" to send all static file to the bucket once set up

*STRIPE_PUBLISHABLE and STRIPE_SECRET
- Publishable and secret Stripe keys
- Required for Stripe functionality
- Available when you create a Stripe account

6. Also you will need to create your own super user so use the command "python3 manage.py createsuperuser" to do so

7. Also if you have taken my whole repo you will need to go into setting.py and remove the # from import env so that the env.py file can be retrieved also do both commands in the terminal "python3 manage.py makemigrations" and "python3 manage.py migrate", now the whole project should be ready to run locally but to make life easier find your .bash_aliases file, you might have to show hidden files and in that file add:
"alias run="python3 manage.py runserver $IP:$C9_PORT" but next do:
.~/.bash_aliases 
in the terminal to reload the file, so then just type run in your terminal to run the whole project.


Run on Heroku

1. First start a new project in Heroku and call it whatever you want, once made head over to resources and in add ons type progres, add this data base.

2. Next head over to settings and reveal vars, copy your progres var key, then go over to your env.py file and add:
os.environ.setdefault("DATABASE_URL", "<key here>")
where it says key here put your key here

3. Also in your terminal use both command sudo pip3 install dj-database-url and sudo pip3 install psycopg2 so that we can connect to the progres database on Heroku

4. You will next need to add import dj_database_url to your setting.py file and comment out your sqlite3 database and replace it with:
DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
also if have already changed your secret key to run through your env.py file don't worry otherwise you will need to do this

5. Next we will need to hook up out aws bucket, so in your settings.py file add the following:

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}

AWS_STORAGE_BUCKET_NAME = 'web name here'
AWS_S3_REGION_NAME = 'your own region here'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

6. After this we will want to add a cutomer storage for files such as image and so on. First in your terminal use command "sudo pip3 install boto3", then on the top level create a custom_storages.py file and in this file add:

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    
7. Next head back over to settings.py file and add:

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

8. Now we need to add our Procfile and requirements file to tell heroku what we need to run the app. lets first start will the Procfile, so first in the terminal use the command "sudo pip3 install gunicorn" and on the top level add a Profile and in this file add:

web: gunicorn <name of project>.wsgi:application

9. Now for the requirements.txt file just use the command "sudo pip3 freeze –local > requirements.txt" in the terminal

10. before we are done here in the IDE, go to your settings.py file and in allowed hosts add '<name of project>.herokuapp.com', this will allow the app to run, also # out your import env in setting.py because we don't need this for Heroku, so git add this all to your github repo.

11. Finally head over to Heroku, go to settings and reveal vars. Here we need to add all our keys, where you need to include will as follow and can be found in your env.py file:

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
SECRET_KEY
STRIPE_PUBLISHABLE
STRIPE_SECRET

also add DISABLE_COLLECTSTATIC will a key of 1

12. Now you can connect your Heroku to your github and deploy the project through github repo


##### Testing

1.	Links
- All nav bar links work 
- All button links work such as submit button for username and the add/edit/delete recipe buttons, they redirect to the correct pages or perform the    correct function
    
2.	Text and colours
- They are appropriately sized and colour scheme is simple and readable
    
3. layout
- layout is responsive across all elements thanks to bootstrap
    
4.	Mobile and browser testing
- I tested the application on the smaller screen devices and tablets, the application performs the same but layout may be different due to smaller      screen and i achieved this by the responsive design of bootstrap. i also performed all the test i stated above on mobile and tablet and i got the     same results
- Application works on all latest and main browsers 

5. Search filter function
- The correct results display
    
6. User SignUp/SignIn
- The application performs the correct processes which is being asked of it
- new users are added admin panel
- user can login and logout with ease

7. Posting reviews
- after posting new review, it added straight away with correct information

8. Store/cart/checkout
- tested adding all products, removing products, adjusting quantity of products and application performs correctly
- checkout work i used the stripe testing payment details and the payments are made to stripe
- also orders are add to admin panel
- Evidence of this can be found in the mockups folder in the repo
9. test.py
- There are some tests made on test.py file across project

#### Credits

Photos were taken from google image some were adjusted using software

Use of Font-Awesome and Boostrap theme:
https://bootswatch.com/3/cerulean/










