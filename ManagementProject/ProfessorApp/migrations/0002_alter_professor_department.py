# Generated by Django 4.0.1 on 2022-01-05 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DepartmentApp', '0001_initial'),
        ('ProfessorApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='department',
            field=models.ManyToManyField(related_name='department_pro', to='DepartmentApp.Department'),
        ),
    ]
