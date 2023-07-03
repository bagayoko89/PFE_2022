# Generated by Django 4.0.5 on 2022-06-24 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ishikawa', '0008_cause_milieu_cause_methode_cause_matiere_cause_main'),
        ('whys', '0016_alter_why5_me_cons'),
    ]

    operations = [
        migrations.CreateModel(
            name='Why_mac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('why1', models.CharField(max_length=500, null=True)),
                ('why2', models.CharField(max_length=500, null=True)),
                ('why3', models.CharField(max_length=500, null=True)),
                ('why4', models.CharField(max_length=500, null=True)),
                ('why5', models.CharField(max_length=500, null=True)),
                ('cons', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ishikawa.cause_machine')),
            ],
        ),
        migrations.DeleteModel(
            name='Why1_mac',
        ),
    ]
