# Generated by Django 3.2.20 on 2023-09-15 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_profile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_staff',
        ),
    ]