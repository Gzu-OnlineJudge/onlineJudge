# Generated by Django 2.2.1 on 2020-04-04 07:10

import Contest.feild
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchrank',
            name='acNum',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='matchrank',
            name='rank',
            field=Contest.feild.ListFiled(blank=True, default='[]', max_length=500),
        ),
    ]
