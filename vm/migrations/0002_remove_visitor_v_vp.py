# Generated by Django 2.2.7 on 2020-01-04 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='v_vp',
        ),
    ]
