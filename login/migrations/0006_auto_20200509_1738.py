# Generated by Django 2.2.7 on 2020-05-09 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20200508_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='channel',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]
