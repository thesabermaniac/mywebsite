from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime

EDUCATION_LEVEL_CHOICES = (
    ('HS', 'High School'),
    ('AA', 'Associate\'s of Arts'),
    ('AS', 'Associate\'s of Science'),
    ('BA', 'Bachelor\'s of Arts'),
    ('BS', 'Bachelor\'s of Science'),
    ('MA', 'Master\'s of Arts'),
    ('MS', 'Master\'s of Science'),
    ('PhD', 'Doctorate Degree'),
    ('O', 'Other'),
)

CLUB_ROLE_CHOICES = (
    ('F', 'Founder'),
    ('P', 'President'),
    ('VP', 'Vice President'),
    ('D', 'Director'),
    ('M', 'Member'),
    ('O', 'Other'),
)

LEVEL_OF_EXPERTISE = (
    ('N', 'Novice'),
    ('I', 'Intermediate'),
    ('A', 'Advanced'),
    ('E', 'Expert'),
)

CATEGORIES = (
    ('WD', 'Web Development'),
    ('OO', 'Object Oriented'),
)


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    email_address = models.EmailField(blank=True)
    phone_number = PhoneNumberField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Experience(models.Model):
    company = models.CharField(max_length=50)
    job_description = models.CharField(max_length=200)
    start_date = models.DateField('start_date', blank=True)
    end_date = models.DateField('end_date', blank=True)
    is_visible = models.BooleanField(default=True)
    is_current = models.BooleanField(default=True)

    def check_current(self):
        if self.end_date < datetime.datetime.now():
            self.is_current = False

    def __str__(self):
        return self.company + ", " + self.job_description


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    role = models.CharField(max_length=20, choices=CLUB_ROLE_CHOICES, default='Member')
    role_description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    school = models.CharField(max_length=50)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    education_level = models.CharField(max_length=20, choices=EDUCATION_LEVEL_CHOICES, default=None)
    currently_enrolled = models.BooleanField(default=False)
    year_started = models.DateField('start_year', blank=True, null=True)
    year_ended = models.DateField('end_year', blank=True, null=True)
    expected_end_year = models.DateField('expected_end_year', blank=True, null=True)
    major = models.CharField(max_length=50, blank=True, null=True)
    major_gpa = models.FloatField(blank=True, null=True)
    overall_gpa = models.FloatField(blank=True, null=True)
    courses = models.ManyToManyField(Course, blank=True)
    clubs = models.ManyToManyField(Club, blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.school


class Skill(models.Model):
    name = models.CharField(max_length=20)
    level_of_expertise = models.CharField(max_length=10, choices=LEVEL_OF_EXPERTISE, default=None)
    description = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORIES, default=None, blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.level_of_expertise + " " + self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    demonstrated_skill = models.ManyToManyField(Skill, blank=True)
    github_link = models.URLField(max_length=200, blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name


"""
class Resume(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    overview = models.CharField(max_length=200, blank=True)
    education = models.ManyToManyField(Education, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    projects = models.ManyToManyField(Project, blank=True)
    experience = models.ManyToManyField(Experience, blank=True)
    is_visible = models.BooleanField(default=True)
    """
