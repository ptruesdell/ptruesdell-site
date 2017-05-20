# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.CharField(max_length=255)
    tags = models.CharField(max_length=500) # used to convey list of technical tools used
    #image = models.ImageField(upload_to='./mysite/static/', height_field=None, width_field=None, max_length=100)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

class Meta:
    # TODO: manually set created dates for each project
    ordering=['-created']

    def __unicode__(self):
    	return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('portfolio.project', args=[self.slug])
