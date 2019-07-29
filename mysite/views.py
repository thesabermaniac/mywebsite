from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader


def index(request):
    template = loader.get_template('resume/home.html')
    return HttpResponse(template.render())
