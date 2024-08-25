Tutorial: https://youtu.be/Rp5vd34d-z4?si=T5xJbebU9a9Rqrmb
Shortcuts of html template in django: ctrl+, 
    emmet: emmet include languages
        add item -> django-html 
        value -> html

Chapter 1: Introduction
-----------------------
step-1: create a project
    django-admin startproject myproject
step-2: goto the main project directory
step-3: run the server
    py manage.py runserver
step-4: from main project directory open 'urls.py' and add paths into the 'urlpatterns' list. E.g.; homepage, about etc.
    note: these are the page routes
step-5: create views for the paths or pages. 
    E.g.; homepage(request):
             return HttpResponse("Hellow World")
step-6: goto urls.py and import views.py then add the views to the specific paths
    E.g.; from . import views
          path('',views.homepage), 2nd parameter is callback function
          path('about/',views.about), etc
step-7: step (1-6) is very basic just showing text as a website, now from this step-7 we will create different webpage using html,css and js
    goto main project directory and create a directory 'templates'
step-8: create different html files
    E.g.; inside templates create homepage.html
step-9: telling django where templates are
    goto setting.py inside this TEMPLATES[
    'DIR':['templates']    
    ]
step-10: now implement the templates inside the views.py
    from django.shortcuts import render
    def homepage(request):
        return render(request, 'home.html')
    def about(request):
        return render(request, 'about.html')
step-11: to add css and js to html files create a directory named 'static' in the main project directory;
    why static? because this directory contains staic assets
    create css and js directory
    inside css create style.css
step-12: telling django where the static files are located; for this goto settings.py and under neth 'STATIC_URL' add a line: 
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR,'staic')
    ]
step-13: now implement the css on html files
    1st-> load the 'staic' folder just under the <!DOCTYPE html> 
        {% load static %}
    2nd-> link the: 
        css file <link rel="stylesheet" href="{% static 'css/style.css' %}">
        and js file <script src = "{% static 'js/main.js' %}" defer></script>
            here 'defer' means load this script after loading all of the pages load this js

Chapter 2: Apps and Templates
-----------------------------
Apps: Some functions or modules that are independent and can be used for different django project. To be more specific a project has different function. E.g: users, shopping card, etc.
Now we will create an App, named posts
Step-1: py manage.py startapp post; this will create a 'posts' file inside the top-level myproject.
Step-2: now tell django that an App is added: goto second-level myproject, inside this 'INSTALLED APPS' append the file name into the list that is 'posts'
Now for this posts app, we will create views templates
Step-3: View 
        goto 'posts' file and open views.py and create views for this post
            def post_lists(request)
                return(request,'post_list')
Step-4: Templates
        now create html files for the 'posts' for this inside this 'posts' file create 'templates' folder and inside 'templates' folder create 'post_list.html' file
        N.B: We already told django where the templates are
Step-5: actually this 'posts' App should have a urls.py if not then manually create inside this
    copy this lines of code from myproject -> urls.py:
    from django.urls import path
    from . import views
    urlpatterns = [
    path('', views.posts_list), #posts_list is a callback function
    ]
Step-6: 













Chapter 3: Models and Migrations
--------------------------------

Chapter 4: Django ORM
---------------------

Chapter 5: Django ORM
---------------------

Chapter 6: Pages URLs and Slugs
-------------------------------

Chapter 7: Upload Images
------------------------

Chapter 8: Challenge
---------------------