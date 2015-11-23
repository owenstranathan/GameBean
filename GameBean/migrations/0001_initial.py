# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100000, blank=True)),
                ('image_url', models.CharField(max_length=1000, blank=True)),
                ('giant_bomb_link', models.CharField(max_length=1000, blank=True)),
                ('website', models.CharField(max_length=1000, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateTimeField(blank=True)),
                ('image_url', models.CharField(max_length=1000, blank=True)),
                ('description', models.CharField(max_length=100000, blank=True)),
                ('giant_bomb_link', models.CharField(max_length=1000, blank=True)),
                ('company', models.ForeignKey(to='GameBean.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100000, blank=True)),
                ('image_url', models.CharField(max_length=1000, blank=True)),
                ('release_date', models.DateTimeField(blank=True)),
                ('giant_bomb_link', models.CharField(max_length=1000, blank=True)),
                ('company', models.ForeignKey(to='GameBean.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=200, blank=True)),
                ('text', models.CharField(max_length=200, blank=True)),
                ('game', models.ForeignKey(to='GameBean.Game')),
                ('reviewer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='platforms',
            field=models.ManyToManyField(to='GameBean.Platform'),
        ),
    ]
