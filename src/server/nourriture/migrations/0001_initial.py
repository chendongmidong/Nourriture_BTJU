# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(max_length=254, null=True)),
                ('price', models.IntegerField(null=True)),
                ('heat', models.FloatField()),
                ('protein', models.FloatField()),
                ('fat', models.FloatField()),
                ('carbohydrate', models.FloatField()),
                ('vitamin', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(max_length=254, null=True)),
                ('preparationTime', models.IntegerField()),
                ('backingTime', models.IntegerField()),
                ('howmanypeoples', models.IntegerField(null=True)),
                ('count_view', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe_Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('ingredient', models.ForeignKey(to='nourriture.Ingredient')),
                ('recipe', models.ForeignKey(to='nourriture.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Religious',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=42, unique=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='nourriture.Recipe_Ingredient', to='nourriture.Ingredient'),
        ),
    ]
