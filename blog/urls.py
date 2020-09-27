from django.urls import path

from . views import *

urlpatterns = [
    # home page url
    path('home/', index, name='home'),
    #about page url
    path('about/', about, name='about'),
    #post page url
    path('post/', post, name='post'),
    #category page url
   
    path('contact/', contact, name='contact'),
    #redirect home/ or 8080:
    path('', home),

    #about url
    path('about/', about),

]
