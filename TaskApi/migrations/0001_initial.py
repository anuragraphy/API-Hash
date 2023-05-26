# Generated by Django 3.2.14 on 2023-05-24 16:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now=True)),
                ('taskName', models.CharField(max_length=100)),
                ('impact', models.IntegerField()),
                ('ease', models.IntegerField()),
                ('confidence', models.IntegerField()),
                ('average', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
