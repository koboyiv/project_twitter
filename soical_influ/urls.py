
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from pages.views import index, contact

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^contact/$', contact, name='contact'),
]
