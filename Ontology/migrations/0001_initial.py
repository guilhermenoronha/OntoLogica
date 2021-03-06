# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-09 19:36
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ontology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('size', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5120)])),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(default='', upload_to=b'')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
