# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.

def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)

    # return the rendered template
    return render(request, 'blog/index.html', {'posts':posts})

def post(request, slug):
    # get the post object
    post = get_object_or_404(Post, slug=slug)

    # return the rendered template
    return render(request, 'blog/post.html', {'post':post})
