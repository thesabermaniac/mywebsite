# Generated by Django 2.1.7 on 2019-07-29 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20190729_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='major_gpa',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='overall_gpa',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
