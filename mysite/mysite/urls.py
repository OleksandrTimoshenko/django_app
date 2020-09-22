from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]


# https://stackoverflow.com/questions/46210934/importerror-couldnt-import-django