# Generated by Django 3.2.19 on 2023-06-28 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elevators', '0004_alter_elevatorrequest_elevator'),
    ]

    operations = [
        migrations.AddField(
            model_name='elevator',
            name='next_destination',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
