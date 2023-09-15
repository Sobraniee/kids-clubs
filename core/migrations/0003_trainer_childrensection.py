# Generated by Django 4.2.4 on 2023-09-15 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_name', models.CharField(max_length=100)),
                ('trainer_last_name', models.CharField(max_length=100)),
                ('trainer_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ChildrenSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_club', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('club_kinds', models.CharField(choices=[('развитие', 'Развитие'), ('спорт', 'Спорт'), ('искусство', 'Искусство')], max_length=20)),
                ('trainer', models.ManyToManyField(related_name='секции', to='core.trainer')),
            ],
        ),
    ]
