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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=254, null=True)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe_Ingredient',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('ingredient', models.ForeignKey(to='nourriture.Ingredient')),
                ('recipe', models.ForeignKey(to='nourriture.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredient',
            field=models.ManyToManyField(through='nourriture.Recipe_Ingredient', to='nourriture.Ingredient'),
        ),
    ]
