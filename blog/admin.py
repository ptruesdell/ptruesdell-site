# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
	# fields display on changed list
	list_display = ['title', 'description']

	#fields to filter the change list with
	list_filter = ['published', 'created']

	# fields to search in change list
	search_field = ['title', 'description', 'content']

	# enable the date drill down on change list
	date_hierarchy = 'created'

	#enable the save buttons on top of change form
	save_on_top = True

	#prepopulate the slug from the title
	prepopulated_fields = {"slug":("title",)}

# Register your models here.
admin.site.register(Post, PostAdmin)
