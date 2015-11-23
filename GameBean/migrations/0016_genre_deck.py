# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameBean', '0015_game_deck'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='deck',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
