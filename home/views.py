# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from home.models import Home

# Create your models here
def home_index(request):
    # get the published home page components
    homepage_items = Home.objects

    # return the rendered template
    return render(request, 'home/home.html', {'homepage_items':homepage_items})
