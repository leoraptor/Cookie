# Cookie
the settings and url.py are the main connections in the application you created


here is the main urls.py code 

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('anothercookiee.urls')),
    path('hello/',include('cookieapli.urls')),
    path('admin/', admin.site.urls),
]

#use this as main urls the url which is under the settings
