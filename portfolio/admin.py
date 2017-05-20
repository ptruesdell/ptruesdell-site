# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from portfolio.models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    # fields display on changed list
    list_display = ['title', 'description']

    # field to filter the change list with
    list_filter = ['published', 'created']

    # field to search in changed list
    search_field = ['title', 'description', 'content']

    # enable the date drill down on change list
    date_hierarchy = 'created'

    # enable the save buttons on top of change form
    save_on_top = True
    
    # prepooulate the slug field
    prepopulated_fields = {"slug":("title",)}
    
# register models
admin.site.register(Project, ProjectAdmin)
