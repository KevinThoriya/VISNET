# Generated by Django 2.2.7 on 2020-02-15 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vm', '0004_auto_20200201_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='v_image',
            field=models.ImageField(default='', upload_to='ids/display_pic'),
        ),
    ]