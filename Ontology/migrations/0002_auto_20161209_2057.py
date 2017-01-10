# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-09 20:57
from __future__ import unicode_literals

import Ontology.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ontology', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ontology',
            name='size',
        ),
        migrations.AlterField(
            model_name='ontology',
            name='file',
            field=models.FileField(default='', upload_to=b'', validators=[Ontology.models.validate_file_extension]),
        ),
    ]
