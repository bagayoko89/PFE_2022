# Generated by Django 4.0.5 on 2022-06-21 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ishikawa', '0005_remove_main_oeuvre_analyse'),
    ]

    operations = [
        migrations.CreateModel(
            name='cause_machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
                ('cause', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ishikawa.macine')),
            ],
        ),
    ]