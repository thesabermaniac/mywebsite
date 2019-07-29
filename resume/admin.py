from django.contrib import admin

from .models import Person, Experience, Course, Club, Education, Skill, Project

admin.site.register(Person)
admin.site.register(Experience)
admin.site.register(Course)
admin.site.register(Club)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Project)
#admin.site.register(Resume)


# Register your models here.
