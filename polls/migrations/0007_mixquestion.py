# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-13 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20160331_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mixquestion',
            fields=[
                ('q_id', models.IntegerField(primary_key=True, serialize=False)),
                ('all_id', models.IntegerField(blank=True, null=True)),
                ('q_text', models.TextField(blank=True, null=True)),
                ('option1', models.TextField(blank=True, null=True)),
                ('option2', models.TextField(blank=True, null=True)),
                ('option3', models.TextField(blank=True, null=True)),
                ('option4', models.TextField(blank=True, null=True)),
                ('ans', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'MixQuestion',
            },
        ),
    ]
