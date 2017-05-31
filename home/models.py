# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Home(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)
	description = models.CharField(max_length=255)
	#image = models.ImageField(upload_to='./mysite/static/', height_field=None, width_field=None, max_length=100)
'''
class HomePanel(models.Model):
	title = models.CharField(max_length=255)
	

# Represents data to be displayed in a panel
class ContentGroup(models.Model):
'''	

class Meta:
    def __unicode__(self):
    	return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('portfolio.project', args=[self.slug])
