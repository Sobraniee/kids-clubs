# Generated by Django 4.2.4 on 2023-09-17 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_rename_trainers_childrensection_trainer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='childrensection',
            old_name='trainer',
            new_name='trainers',
        ),
    ]