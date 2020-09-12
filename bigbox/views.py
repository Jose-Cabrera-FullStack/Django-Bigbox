from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from django.shortcuts import render, get_object_or_404, reverse
from bigbox.models import Box, Activity
from django.core.paginator import Paginator
from django.http import (HttpResponsePermanentRedirect)

def redirect(request):
    return HttpResponsePermanentRedirect(reverse('box'))

def box(request):
    # List existing boxes
    boxes = Box.objects.all()
    return render(request,'box.html',{'boxes':boxes})

def box_id(request, id):
    # List existing box_id
    box = Box.objects.filter(id=id)
    return render(request,'box-id.html',{'box':box})

def box_activity(request, id):
    # List existing box_activity
    activities = Box.objects.filter(pk=id)
    activity=activities.all()
    paginator = Paginator(activity,20)
    page_obj = request.GET.get('page')
    activities=paginator.get_page(page_obj)
    return render(request,'box-activities.html',{'activities':activities})

def activity(request, id, section):
    # List existing activity
    activity = Activity.objects.filter(id=section)
    paginator = Paginator(activity,20)
    page_obj = request.GET.get('page')
    activity=paginator.get_page(page_obj)
    return render(request,'activity.html',{'activity':activity})

def slug(request, slug):
    # List existing slug
    box = Box.objects.filter(slug=slug)
    return render(request,'box-id.html',{'box':box})