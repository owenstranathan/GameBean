# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameBean', '0006_auto_20151113_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(max_length=10000, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.CharField(max_length=10000, blank=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='description',
            field=models.CharField(max_length=10000, blank=True),
        ),
    ]
