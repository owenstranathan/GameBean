# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameBean', '0002_auto_20151111_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='api_id',
        ),
        migrations.RemoveField(
            model_name='game',
            name='api_id',
        ),
        migrations.RemoveField(
            model_name='platform',
            name='api_id',
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
