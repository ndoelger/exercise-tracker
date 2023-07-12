# Generated by Django 4.2.3 on 2023-07-07 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='exercise',
            name='directions',
            field=models.TextField(default='direction', max_length=500),
        ),
        migrations.AddField(
            model_name='exercise',
            name='intensity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exercise',
            name='musclegroups',
            field=models.CharField(default='Musclegroup', max_length=100),
        ),
        migrations.AddField(
            model_name='exercise',
            name='name',
            field=models.CharField(default='Exercise', max_length=100),
        ),
    ]
