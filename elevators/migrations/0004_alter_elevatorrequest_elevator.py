# Generated by Django 3.2.19 on 2023-06-28 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elevators', '0003_auto_20230628_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevatorrequest',
            name='elevator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='elevators.elevator'),
        ),
    ]