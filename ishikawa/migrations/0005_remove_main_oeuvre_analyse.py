# Generated by Django 4.0.5 on 2022-06-21 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ishikawa', '0004_rename_machine_macine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main_oeuvre',
            name='analyse',
        ),
    ]