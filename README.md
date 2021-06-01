# My Beginner notes

### Creating a requirement.txt
1. I am using venv so no pipfile.lock etc
2. $ pip3 freeze > requirements.txt

### Starting a project : Page 18-19
$ django-admin startproject config .
1. The config/settings.py file controls our project’s settings
2. urls.py tells Django which pages to build in response to a browser or URL request, and 
3. wsgi.py, which stands for Web Server Gateway Interface helps Django serve our eventual web pages
4. manage.py executes various Django commands such as running the local web server or creating a new app
5. asgi.py allows for an optional Asynchronous Server Gateway Interface34 to be run.

### Migration : Page 21
$ manage.py migrate
1. Django is complaining that we have not yet migrated, or configured, our initial database

### Creating the first app : Page 22-23
$ python manage.py startapp appname
1. admin.py     : Configuration file for the built-in Django Admin app, where we register our model
2. apps.py      : Configuration file for the app itself
3. /migrations  : Keep track of any changes to the models file so it sync with the database (sqlite3)
4. tests.py     : Testing for the current app
5. views.py     : Handle the respone/request logic for the webapp

### Add your app to the config/settings.py : Page 24
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages', # Adding the newly created app  <--- Add here
]
```
1. The URLpattern specifies a view which then determines the content for the page (usually from a database model) and then ultimately a template for styling and basic logic. The end result is sent back to the user as an HTTP response.
- URL -> View -> Model (typically) -> Template
2. Meaning that django takes in 4 files for a given page, 3 files if model is not needed
3. views    : Determine which content to be displayed on the given page
4. URLConfs : Determine where the page is going
5. mdoel    : contains the content from the database
6. template : styling for the content

### Edit the pages/views.py
```
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    return HttpResponse('This works')
```

### Creating a urls.py in your app
1. $ type nul > urls.py
2. Add the following item
```
from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home'), 
]
```

### Update config/urls.py
1. After creating the app and set up the urls on the app, we need to add pages.urls into the config/urls.py
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')) # Newly added
]
```
2. When the user request for a url, it will first go to the config/urls.py to check the url, is the url exists, it will go to the specified apps' urls.py to check the sub url then response with a view of the app

### Git
$ git init      : Initialize it.
$ git status    : Checking the current status of the working directory
$ git add .     : Tracking the current file
$ git add -A    : Adding all the file
$ git commit -m "Message" : Adding the commit msg desc
!!! Note: https://www.youtube.com/watch?v=NRf1LeQju2g for django best practice
$ git push      : Pushing the committed files

### Adding git alias
1. Find .gitconfig under user directory and edit
2. Mine: "C:\Users\Acer\.gitconfig"
```
[alias]
	st = status
	a = add
	b = branch
	c = commit
	co = checkout
	cob = checkout -b
	alias = config --get-regexp alias
```
2. Next time to check status
$ git st

### Creating templates for the views : Page 38
$ cd app
$ mkdir templates

#### Update config/settings.py
1. Tell Django the location of our new templates directory. This is a one-line change to the setting 'DIRS' under TEMPLATES.
```
'DIRS': [str(BASE_DIR.joinpath('templates'))], # Added to link
```

#### Adding some content to the home.html
```
<h1>Testing</h1>
```

#### Configure the views.py of the app
```
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
```

#### Update the urls.py from the config then that of the app
1. config/urls.py
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')) # Newly added
]
```
2. app/urls.py
```
from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), 
]
```
### Give a try : Add an about page
1. Make a about page linking by using the methods we have before
2. Add 'about/' in the urls.py of your app
```
from .views import HomePageView, AboutPage
path('about/', AboutPage.as_view(), name='about'), 
```
Steps: views -> template (add the about.html) -> both urls.py if neccesary 

### Extending Templates : Page 42
Ease the process of repeating content on every page (header, footer, etc).
1. Create a base.html in templates
```
<header>
    <a href="{% url 'home' %}">Home</a>
    <a href="{% url 'about' %}">About</a>
</header>

{% block content %}
{% endblock content %}
```
2. Block tag called content is added, these blocks can be overwritten by child templates via inheritance.
3. It is optional to put the name `content` for the endblock, you can use `{% endblock %}` is enough.
4. Make the home.html and about.html to extend the base.html
```
<!-- Make sure to have the `'` -->
{% extends 'base.html' %} 

{% block content %}
<h1>This is the homepage</h1>
{% endblock %}
```

