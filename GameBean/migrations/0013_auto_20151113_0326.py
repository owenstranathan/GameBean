# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameBean', '0012_auto_20151113_0220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='genre',
            new_name='genres',
        ),
    ]
