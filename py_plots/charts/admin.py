# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from .models import *


admin.site.register(Option)
admin.site.register(PlotFunction)
admin.site.register(Parameter)
admin.site.register(ParameterChoice)
admin.site.register(PlotImage)
