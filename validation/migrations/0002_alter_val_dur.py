# Generated by Django 4.0.5 on 2022-07-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='val',
            name='Dur',
            field=models.IntegerField(null=True),
        ),
    ]
