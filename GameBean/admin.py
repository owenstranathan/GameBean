from django.contrib import admin
from .models import Company, Game, Platform, Review

admin.site.register(Company)
admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(Review)
