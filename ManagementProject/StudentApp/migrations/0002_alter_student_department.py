# Generated by Django 4.0.1 on 2022-01-05 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DepartmentApp', '0001_initial'),
        ('StudentApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_stu', to='DepartmentApp.department'),
        ),
    ]