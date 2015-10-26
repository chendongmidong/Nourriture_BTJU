# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nourriture', '0003_auto_20151025_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='backingTime',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparationTime',
            field=models.IntegerField(null=True),
        ),
    ]
