# Generated by Django 3.2.25 on 2024-06-18 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0006_grades_four_points_scale'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Grades',
        ),
    ]