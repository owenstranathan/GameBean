# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameBean', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='release_date',
            field=models.DateField(blank=True),
        ),
    ]
