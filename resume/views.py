from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Person, Experience, Course, Club, Education, Skill, Project


class ResumeView(generic.ListView):
    model = Person
    template_name = 'resume/resume.html'
    context_object_name = 'person'

    def get_queryset(self):
        return Person.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experiences'] = Experience.objects.all()
        context['courses'] = Course.objects.all()
        context['clubs'] = Club.objects.all()
        context['education'] = Education.objects.all()
        context['skills'] = Skill.objects.all()
        context['projects'] = Project.objects.all()
        return context


class EducationView(generic.ListView):
    model = Education
    template_name = 'resume/education.html'
    context_object_name = 'education'

    def get_queryset(self):
        return Education.objects.all()


# Create your views here.
