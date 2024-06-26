# Generated by Django 3.2.25 on 2024-06-16 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0002_onlineclassroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('grade', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('course_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.courses')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
