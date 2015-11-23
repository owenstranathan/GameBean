# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameBean', '0014_auto_20151122_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='deck',
            field=models.CharField(max_length=10000, null=True, blank=True),
        ),
    ]
