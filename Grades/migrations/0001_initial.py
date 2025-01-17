# Generated by Django 4.0.6 on 2022-08-01 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0002_course_credit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.student')),
            ],
        ),
    ]
