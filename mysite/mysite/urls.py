from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

 # зупинився на Playing with the API в Lesson 2
 # щоб робити налаштування бази данних дивися /mysite/mysite/settings.py    77 строка