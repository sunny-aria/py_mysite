"""py_mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from polls.views import hello,poll_index,poll_edit
from polls import search

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'hello/', hello),
    path(r'search-form/', search.search_form),
    path('search', search.search),
    path('search-post', search.search_post),
    path('poll-index', poll_index),
    path(r'^poll-edit/', poll_edit, name='poll-edit'),
]
