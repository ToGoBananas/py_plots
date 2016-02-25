# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class PlotFunction(models.Model):
    name = models.CharField(max_length=50)
    code = models.TextField()
    parameters = models.ManyToManyField('Parameter', blank=True)
    options = models.ManyToManyField('Option', blank=True)

    def __str__(self):
        return self.name

    def get_images(self):
        return PlotImage.objects.filter(plot=self)


class Option(models.Model):
    name = models.CharField(max_length=50)
    action = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Parameter(models.Model):
    name = models.CharField(max_length=100)
    choices = models.ManyToManyField('ParameterChoice')

    def __str__(self):
        return self.name


class ParameterChoice(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PlotImage(models.Model):
    plot = models.ForeignKey(PlotFunction)
    image = models.ImageField(blank=True, null=True)
