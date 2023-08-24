"""stream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import home.views
import home.views.stream
import home.views.sse

urlpatterns = [
    path('', home.views.chooser),
    path('stream', home.views.stream.index, name='index'),
    path('via-sse', home.views.sse.index, name='index_sse'),
    path('recommend-sse', home.views.sse.handle_sse, name='index_sse'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
