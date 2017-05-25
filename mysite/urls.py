"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from blog.views import index, post
from portfolio.views import portfolio_index, project
from home.views import home_index
from contact_form.views import contact

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_index),
    url(r'^portfolio/', portfolio_index),
	url(r'^portfolio/(?P<slug>[\w\-]+)/$', project),
    url(r'^contact', contact),
    url(r'^blog/', index),
		url(r'^(?P<slug>[\w\-]+)/$', post),
    
]
