# Generated by Django 4.0.5 on 2022-07-04 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro_arrets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='micro',
            name='frequence',
            field=models.IntegerField(null=True),
        ),
    ]
