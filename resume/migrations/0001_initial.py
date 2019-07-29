# Generated by Django 2.1.7 on 2019-07-28 21:08

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('role', models.CharField(choices=[('F', 'Founder'), ('P', 'President'), ('VP', 'Vice President'), ('D', 'Director'), ('M', 'Member'), ('O', 'Other')], default='Member', max_length=20)),
                ('role_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=50)),
                ('education_level', models.CharField(choices=[('HS', 'High School'), ('AA', 'Associates of Arts'), ('AS', 'Associates of Science'), ('BA', 'Bachelors of Arts'), ('BS', 'Bachelors of Science'), ('MA', 'MAsters of Arts'), ('MS', 'Masters of Science'), ('PhD', 'Doctorate Degree'), ('O', 'Other')], default=None, max_length=20)),
                ('currently_enrolled', models.BooleanField(default=False)),
                ('year_started', models.DateField(blank=True, null=True, verbose_name='start_year')),
                ('year_ended', models.DateField(blank=True, null=True, verbose_name='end_year')),
                ('expected_end_year', models.DateField(blank=True, null=True, verbose_name='expected_end_year')),
                ('major', models.CharField(blank=True, max_length=50, null=True)),
                ('major_gpa', models.FloatField()),
                ('overall_gpa', models.FloatField()),
                ('is_visible', models.BooleanField(default=True)),
                ('clubs', models.ManyToManyField(to='resume.Club')),
                ('courses', models.ManyToManyField(to='resume.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('job_description', models.CharField(max_length=200)),
                ('start_date', models.DateField(verbose_name='start_date')),
                ('end_date', models.DateField(verbose_name='end_date')),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=5)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('linkedin', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('github_link', models.URLField()),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overview', models.CharField(max_length=200)),
                ('is_visible', models.BooleanField(default=True)),
                ('education', models.ManyToManyField(to='resume.Education')),
                ('experience', models.ManyToManyField(to='resume.Experience')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Person')),
                ('projects', models.ManyToManyField(to='resume.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('level_of_expertise', models.CharField(choices=[('N', 'Novice'), ('I', 'Intermediate'), ('A', 'Advanced'), ('E', 'Expert')], default=None, max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('category', models.CharField(blank=True, choices=[('WD', 'Web Development'), ('OO', 'Object Oriented')], default=None, max_length=20)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='resume',
            name='skills',
            field=models.ManyToManyField(to='resume.Skill'),
        ),
        migrations.AddField(
            model_name='project',
            name='demonstrated_skill',
            field=models.ManyToManyField(to='resume.Skill'),
        ),
    ]
