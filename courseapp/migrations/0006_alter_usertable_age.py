# Generated by Django 4.2.4 on 2023-10-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0005_alter_usertable_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertable',
            name='age',
            field=models.IntegerField(),
        ),
    ]