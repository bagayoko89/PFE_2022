# Generated by Django 4.0.5 on 2022-06-19 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prob',
            old_name='id_prob',
            new_name='id_problem',
        ),
    ]
