from django.urls import path

from . import views

app_name = 'resume'
urlpatterns =[
    path('', views.ResumeView.as_view(), name='resume'),
    path('education/', views.EducationView.as_view(), name="education"),
]