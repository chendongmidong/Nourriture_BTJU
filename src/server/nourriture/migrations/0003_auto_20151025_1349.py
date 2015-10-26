# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nourriture', '0002_auto_20151019_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='carbohydrate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='fat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='heat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='protein',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='vitamin',
            field=models.FloatField(null=True),
        ),
    ]
