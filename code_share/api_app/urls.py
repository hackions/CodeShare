from django.conf.urls import url, include
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns as suffix


urlpatterns = [
    url(r'^$', api_home, name='api_home'),
    url(r'^(?P<hash_id>\d+)/$', code_by_hash, name='return_by_hash'),
    url(r'^(?P<file_name>[\w-]+)/$', code_by_filename, name='return_by_filename'),
]
urlpatterns=suffix(urlpatterns)