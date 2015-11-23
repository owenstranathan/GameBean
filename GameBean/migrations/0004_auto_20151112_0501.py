# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameBean', '0003_auto_20151112_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image_url',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='image_url',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='image_url',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
