# Generated by Django 4.2.4 on 2023-09-29 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0002_studenttable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studenttable',
            old_name='course',
            new_name='course_id',
        ),
    ]