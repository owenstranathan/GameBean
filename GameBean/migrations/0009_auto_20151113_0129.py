# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameBean', '0008_auto_20151113_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='release_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
