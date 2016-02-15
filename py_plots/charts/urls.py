# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/test/1/')),
    url(
        regex=r'^(?P<script_pk>[0-9]+)/$',
        view=views.ScriptView.as_view(),
        name='test'
    ),
    url(
        regex=r'^(?P<script_pk>[0-9]+)/execute/$',
        view=views.ExecuteView.as_view(),
        name='execute'
    ),
]

