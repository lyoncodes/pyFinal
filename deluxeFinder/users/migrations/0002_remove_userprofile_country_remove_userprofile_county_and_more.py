# Generated by Django 4.0.3 on 2022-03-25 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='county',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='post_code',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='town',
        ),
    ]