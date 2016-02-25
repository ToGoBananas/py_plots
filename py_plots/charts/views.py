# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, View, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render_to_response
from .forms import PlotFunctionForm
from .models import PlotFunction, PlotImage
from pygments import highlight
from pygments.lexers import Python3Lexer
from pygments.formatters import HtmlFormatter
from django.http import HttpResponse
import matplotlib.pyplot as plt
from django.core.files import File
import json
from PIL import Image
import io


class ScriptView(LoginRequiredMixin, TemplateView):
    template_name = 'charts/test.html'

    def get_context_data(self, script_pk, **kwargs):
        context = super(ScriptView, self).get_context_data(**kwargs)
        context['scripts'] = PlotFunction.objects.all()
        context['active_script'] = context['scripts'].get(pk=script_pk)
        # context['code'] = context['active_script'].code
        return context


class ExecuteView(LoginRequiredMixin, View):

    def post(self, request, script_pk):
        code = request.POST['code']
        for x in request.POST:
            if x != 'code':
                code = code.replace(x, request.POST[x])
        exec(code)
        plot = PlotFunction.objects.get(pk=script_pk)
        if plot.get_images():
            plot.get_images().delete()
        for i in plt.get_fignums():
            buf = io.BytesIO()
            plt.figure(i)
            plt.savefig(buf, format='png')
            plot_image = PlotImage.objects.create(plot=plot)
            plot_image.image.save(str(i)+plot.name+'.png', File(buf))
            buf.close()
        for i in plt.get_fignums():
            plt.close(plt.figure(i))
        return render_to_response('charts/script_images.html', {'plot': plot})
