# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import GameBean.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=10000, blank=True)),
                ('image_url', models.CharField(max_length=200, null=True, blank=True)),
                ('giant_bomb_link', models.CharField(max_length=200, blank=True)),
                ('website', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateTimeField(null=True, blank=True)),
                ('image_url', models.CharField(max_length=200, null=True, blank=True)),
                ('deck', models.CharField(max_length=10000, null=True, blank=True)),
                ('description', models.CharField(max_length=100000, blank=True)),
                ('giant_bomb_link', models.CharField(max_length=200, blank=True)),
                ('developers', models.ManyToManyField(to='GameBean.Company')),
            ],
        ),
        migrations.CreateModel(
            name='GameSprout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=GameBean.models.content_file_name)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('games', models.ForeignKey(to='GameBean.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('deck', models.CharField(max_length=5000, null=True)),
                ('description', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=10000, blank=True)),
                ('image_url', models.CharField(max_length=200, null=True, blank=True)),
                ('release_date', models.DateTimeField(null=True, blank=True)),
                ('giant_bomb_link', models.CharField(max_length=200, blank=True)),
                ('company', models.ForeignKey(to='GameBean.Company', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=100000)),
                ('featured', models.BooleanField(default=False)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(to='GameBean.Game')),
                ('reviewer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='gamesprout',
            name='platforms',
            field=models.ForeignKey(to='GameBean.Platform'),
        ),
        migrations.AddField(
            model_name='gamesprout',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(to='GameBean.Genre'),
        ),
        migrations.AddField(
            model_name='game',
            name='platforms',
            field=models.ManyToManyField(to='GameBean.Platform'),
        ),
    ]
