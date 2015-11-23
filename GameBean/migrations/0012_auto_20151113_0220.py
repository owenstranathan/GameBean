# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameBean', '0011_auto_20151113_0153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='company',
        ),
        migrations.AddField(
            model_name='game',
            name='developers',
            field=models.ManyToManyField(to='GameBean.Company'),
        ),
    ]
