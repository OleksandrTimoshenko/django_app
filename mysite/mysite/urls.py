from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]


# https://stackoverflow.com/questions/46210934/importerror-couldnt-import-django
 #  virtualenv newenv
 #  source newenv/bin/activate
 #  pip install django
 #  django-admin --version
 #  
 # do commands
 #
 # deactivate

 # зупинився на Playing with the API в Lesson 2
 # щоб робити налаштування бази данних дивися /mysite/mysite/settings.py    77 строка