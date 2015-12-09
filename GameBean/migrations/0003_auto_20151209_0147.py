# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GameBean', '0002_auto_20151206_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='downVotes',
            field=models.ManyToManyField(related_name='reviews_down_voted', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='upVotes',
            field=models.ManyToManyField(related_name='reviews_up_voted', to=settings.AUTH_USER_MODEL),
        ),
    ]
