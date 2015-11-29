from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(blank=True, max_length=10000)
    image_url = models.CharField(blank=True, null=True, max_length=200)
    giant_bomb_link = models.CharField(blank=True, max_length=200)
    website = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return unicode(self.name)

    def __unicode__(self):
        return self.name

class Genre(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    name = models.CharField(max_length=100)
    deck = models.CharField(null=True, max_length=5000)
    description = models.CharField(max_length=10000)

    def __str__(self):
        return unicode(self.name)

    def __unicode__(self):
        return self.name

class Platform(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    name = models.CharField(blank=False, max_length=100)
    company = models.ForeignKey(Company, null=True)
    description = models.CharField(blank=True, max_length=10000)
    image_url = models.CharField(blank=True, null=True, max_length=200)
    release_date = models.DateTimeField(blank=True, null=True)
    giant_bomb_link = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return unicode(self.name)

    def __unicode__(self):
        return self.name

class Game(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    name = models.CharField(max_length=100)
    developers = models.ManyToManyField(Company)
    platforms = models.ManyToManyField(Platform)
    genres = models.ManyToManyField(Genre)
    release_date = models.DateTimeField(blank=True, null=True)
    image_url = models.CharField(blank=True, null=True, max_length=200)
    deck = models.CharField(blank=True, null=True, max_length=10000)
    description = models.CharField(blank=True, max_length=100000)
    giant_bomb_link = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return unicode(self.name)

    def __unicode__(self):
        return self.name


class Review(models.Model):
    topic = models.CharField(blank=True, max_length=200)
    text = models.CharField(blank=True, max_length=200)
    reviewer = models.ForeignKey(User)
    game = models.ForeignKey(Game)

    def __str__(self):
        return unicode(reviewer.username)


    def __unicode__(self):
        return self.name
