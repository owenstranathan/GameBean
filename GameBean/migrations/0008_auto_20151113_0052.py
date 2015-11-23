# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameBean', '0007_auto_20151113_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='company',
            field=models.ForeignKey(to='GameBean.Company', null=True),
        ),
    ]
