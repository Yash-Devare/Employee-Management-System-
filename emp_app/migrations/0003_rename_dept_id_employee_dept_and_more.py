# Generated by Django 5.0.3 on 2024-11-03 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_rename_dept_employee_dept_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='dept_id',
            new_name='dept',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='role_id',
            new_name='role',
        ),
    ]
