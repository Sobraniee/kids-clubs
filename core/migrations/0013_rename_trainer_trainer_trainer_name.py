# Generated by Django 4.2.4 on 2023-09-17 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_rename_trainer_childrensection_trainers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainer',
            old_name='trainer',
            new_name='trainer_name',
        ),
    ]
