# Generated by Django 3.2.14 on 2023-05-24 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApi', '0003_taskmodel_average'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='average',
            field=models.FloatField(default=0),
        ),
    ]
