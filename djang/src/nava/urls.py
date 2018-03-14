"""nava URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


from navaneethaedu.views import HomeView, AboutView, ContactView

handler404 = 'navaneethaedu.views.handler404'
handler500 = 'navaneethaedu.views.handler500'

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='home'),
    url(r'^contactus/$', ContactView.as_view(), name='contact'),
	url(r'^aboutus/', AboutView.as_view(), name='about'),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
