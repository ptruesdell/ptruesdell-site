# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from portfolio.models import Project

# Create your models here
def portfolio_index(request):
    # get the project that are published
    projects = Project.objects.filter(published=True)

    # return the rendered template
    return render(request, 'portfolio/portfolio_index.html', {'projects':projects})


def project(request, slug):
    # get the project object
    project = get_object_or_404(Project, slug=slug)

    # return the rendered template
    return render(request, 'portfolio/project.html', {'project':project})
