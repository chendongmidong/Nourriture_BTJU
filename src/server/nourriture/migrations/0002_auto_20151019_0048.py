# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nourriture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alergie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=42)),
                ('description', models.TextField(null=True)),
                ('forbidden_ingredients', models.ManyToManyField(to='nourriture.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Intolerence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=42)),
                ('description', models.TextField(null=True)),
                ('forbidden_ingredients', models.ManyToManyField(to='nourriture.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=42)),
                ('description', models.TextField(null=True)),
                ('forbidden_ingredients', models.ManyToManyField(to='nourriture.Ingredient')),
            ],
        ),
        migrations.DeleteModel(
            name='Religious',
        ),
    ]
