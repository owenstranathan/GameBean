# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameBean', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamesprout',
            name='games',
        ),
        migrations.AddField(
            model_name='gamesprout',
            name='games',
            field=models.ManyToManyField(to='GameBean.Game'),
        ),
        migrations.RemoveField(
            model_name='gamesprout',
            name='platforms',
        ),
        migrations.AddField(
            model_name='gamesprout',
            name='platforms',
            field=models.ManyToManyField(to='GameBean.Platform'),
        ),
    ]
