# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nourriture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe_ingredient',
            name='recipe',
            field=models.ForeignKey(to='nourriture.Recipe'),
        ),
    ]
