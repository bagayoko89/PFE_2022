# Generated by Django 4.0.5 on 2022-06-23 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ishikawa', '0008_cause_milieu_cause_methode_cause_matiere_cause_main'),
        ('whys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Why1',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=500, null=True)),
                ('cons', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ishikawa.cause_machine')),
            ],
        ),
        migrations.DeleteModel(
            name='Why',
        ),
    ]
