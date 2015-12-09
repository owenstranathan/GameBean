# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameBean', '0003_auto_20151209_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
