# Generated by Django 4.0.1 on 2022-01-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DepartmentApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor_name', models.CharField(max_length=32)),
                ('salary', models.IntegerField()),
                ('department', models.ManyToManyField(to='DepartmentApp.Department')),
            ],
        ),
    ]