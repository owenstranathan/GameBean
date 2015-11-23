# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameBean', '0005_auto_20151112_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(max_length=5000, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='giant_bomb_link',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='image_url',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.CharField(max_length=5000, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='giant_bomb_link',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='image_url',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='description',
            field=models.CharField(max_length=5000, blank=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='giant_bomb_link',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='image_url',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='release_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
