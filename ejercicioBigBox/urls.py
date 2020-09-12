"""ejercicioBigBox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from bigbox import views as bigbox_views
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(
        'admin/', 
        admin.site.urls,
        name='admin'),
    path(
        '', 
        bigbox_views.redirect,
        name=''),

    path(
        'box/', 
        bigbox_views.box,
        name='box'),

    path(
        'box/<int:id>/', 
        bigbox_views.box_id,
        name='box_id'),

    path('box/<int:id>/activity', 
        bigbox_views.box_activity,
        name='activities'),

    path('box/<int:id>/activity/<int:section>', 
        bigbox_views.activity,
        name='activity'),

    path('box/<str:slug>', 
        bigbox_views.slug,
        name='slug'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
