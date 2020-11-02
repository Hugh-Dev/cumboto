
from __future__ import unicode_literals
from django.conf.urls import include, url
from base.views import inicio

urlpatterns = [
    url(r'^inicio/$', 'base.views.inicio', name='inicio'),
]