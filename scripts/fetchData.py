#!/usr/bin/python
#-*- coding: utf-8 -*-

## NOTE: MUST BE RUN FROM DJANGO SHELL

import requests
import json
import sys
import traceback
import pytz
import time

from GameBean.models import Company, Platform, Game, Genre
from django.utils.dateparse import parse_datetime
from django.core.exceptions import ImproperlyConfigured

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)



api_url = "http://www.giantbomb.com/api/"
api_key = get_env_variable(API_KEY)
encoding_format = 'json'


fields = {
    "games" : ("api_detail_url", "original_release_date",),
    "game" : ("id", "name", "developers", "platforms","genres", "image", "deck", "description", "site_detail_url",),
    "company" : ("id", "name", "deck", "image", "site_detail_url", "website",),
    "platform" : ("id", "name", "company", "deck", "image", "release_date", "site_detail_url",),
    "genres" : ("id", "api_detail_url",),
    "genre" : ("name", "deck", "description"),
}

resources = {
    "games" : 'games/',
    "company" : 'companies/',
    "platform" : 'platforms/',
    "genres" : 'genres/',
}

def insertGame(id,name,developers,platforms,genres,description,image_url,release_date,giant_bomb_link):
    release_date_time = parse_datetime(release_date)
    if release_date_time:
        release_date_time = pytz.utc.localize(release_date_time)
    game = Game(id=id, name=name, description=description, image_url=image_url, release_date=release_date_time, giant_bomb_link=giant_bomb_link)
    game.save()

    for dev_id in developers:
        try:
            developer = Company.objects.get(id=dev_id)
        except companies.DoesNotExist:
            developer = Company.objects.get(name="None")
        game.developers.add(developer)

    for plat_id in platforms:
        try:
            platform = Platform.objects.get(id=plat_id)
        except Platform.DoesNotExist:
            platform = Platform.objects.get(name="None")
        game.platforms.add(platform)
    for gen_id in genres:
        try:
            genre = Genre.objects.get(id=gen_id)
        except Genre.DoesNotExist:
            genre = Genre.objects.get(name="None")
        game.genres.add(genre)
    game.save()

def onGame(json_object, offset):
    for element in json_object:
        try:
            # print offset
            payload = {
                'format': encoding_format,
                'api_key' : api_key,
                'field_list' : ",".join(fields["game"]),
                'offset' : offset,
                }
            url = element["api_detail_url"]
            r = requests.get(url, params=payload)
            json = r.json()
            print json["error"]
            results = json["results"]
            print results
            id = results["id"]
            name = unicode(results["name"])
            developers = []
            if results["developers"] is not None:
                for dev in results["developers"]:
                    developers.append(int(dev["id"]))

            platforms = []
            if results["platforms"] is not None:
                for plat in results["platforms"]:
                    platforms.append(int(plat["id"]))

            genres = []
            if results["genres"] is not None:
                for gen in results["genres"]:
                    genres.append(int(gen["id"]))

            description = results["description"] if results["description"] is not None else ""
            image_url = results["image"]["medium_url"] if results["image"] is not None else ""
            release_date = element["original_release_date"] if element["original_release_date"] is not None else ""
            giant_bomb_link = results["site_detail_url"] if results["site_detail_url"] is not None else ""

            insertGame(id, name, developers, platforms, genres, description, image_url, release_date, giant_bomb_link)
            offset = str(int(offset) + 1)

        except:
            offset = str(int(offset) + 1)

        # offset = str(int(offset) + 1)

        time.sleep(3)

    return offset






#Company fields:
# API:
## id
## name
## description
## image -> medium_url
## site_detail_url
## website
#
#MODEL
## id
## name
## description
## image_url
## giant_bomb_link
## website

def insertCompany(id, name, description, image_url, giant_bomb_link, website):
    description = (description[:9997] + "...") if len(description) > 10000 else description
    company = Company(id=id, name=name, description=description,giant_bomb_link=giant_bomb_link, website=website)
    company.save()

def onCompany(json_object, offset):
    for element in json_object:
        print offset
        id = element["id"]
        name = unicode(element["name"])
        print name
        description = unicode(element["deck"] if element["deck"] != None else "")
        image_url = element["image"]["medium_url"] if element["image"] != None else ""
        giant_bomb_link = element["site_detail_url"]
        website = element["website"] if element["website"] != None else ""
        insertCompany(int(id), name, description, image_url, giant_bomb_link, website)
        offset = str(int(offset)+1)

    return offset


#API
##id
##name
##company
##description
##image
##release_date
##site_detail_url

#Model
##id
##name
##company
##description
##image_url
##release_date
##giant_bomb_link

def insertPlatform(id, name, company_id, description, image_url, release_date, giant_bomb_link):
    print "Inserting platform " , name
    description = (description[:9997] + "...") if len(description) > 10000 else description
    company = None
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist:
        company = Company.objects.get(name="None")

    release_date_time = parse_datetime(release_date)
    platform = Platform(id, name, company.id, description, image_url, release_date_time, giant_bomb_link)
    platform.save()


def onPlatform(json_object, offset):
    for element in json_object:
        id = element["id"]
        print id
        name = unicode(element["name"])
        print name
        company_id = element["company"]["id"] if element["company"] is not None else None
        description = element["deck"] if element["deck"] is not None else ""
        image_url = element["image"]["medium_url"] if element["image"] is not None else ""
        release_date = element["release_date"] if element["release_date"] is not None else ""
        giant_bomb_link = element["site_detail_url"] if element["site_detail_url"] is not None else ""
        insertPlatform(int(id), name, company_id, description, image_url, release_date, giant_bomb_link)
        offset = str(int(offset) + 1)

    return offset


def insertGenre(id, name, deck, description):
    genre = Genre(id, name, deck, description)
    genre.save()
    print genre


def onGenre(json_object, offset):
    for element in json_object:
        print element
        payload= {
            'format': encoding_format,
            'api_key' : api_key,
            'field_list' : ",".join(fields["genre"]),
        }
        id = element["id"]
        url = element["api_detail_url"]
        print id
        r = requests.get(url, params=payload)
        json = r.json()
        results = json["results"]
        print results
        name = unicode(results["name"])
        deck = unicode(results["deck"])
        description = unicode(results["description"]) if results["description"] != None else ""
        insertGenre(int(id), name, deck, description)
        offset = str(int(offset) + 1)

    return offset



what_to_do = {
    "games" : onGame,
    "company" : onCompany,
    "platform" : onPlatform,
    "genres" : onGenre,
}

number_of_records_to_fetch = {
    "games" : 47368,
    "company" : 11069 ,
    "platform" : 145 ,
    "genres" : 50,
}


def loadData(resource, offset):
    try:
        while(int(offset) < number_of_records_to_fetch[resource]):
            print offset
            payload = {
                'format': encoding_format,
                'api_key' : api_key,
                'field_list' : ",".join(fields[resource]),
                'offset' : offset,
            }
            print "Percent complete: "
            print "about to request"
            print api_url+resources[resource]
            # print params
            r = requests.get(api_url+resources[resource], params=payload)
            print r.url
            json = r.json()
            print "Json in"
            results = json["results"]
            print "Results found: ", len(results)
            # print "Sleeping for 30 seconds"
            # for i in range(30):
            #     sys.stdout.write("time: %d   \r" % (i) )
            #     sys.stdout.flush()
            #     time.sleep(1)
            offset = what_to_do[resource](results, offset)
            print offset

        #done without exception
        print offset, " records successfully inserted!"


    except:
        print "Exception thrown: "
        e = sys.exc_info()
        print "Error: ", e[0], e[1], traceback.print_tb(e[2])








# if __name__ == '__main__':
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SuperAwesomeGameDatabase.settings")
#     import django
#     django.setup()
#     from GameBean.models import Company, Platform, Game
#     for arg in sys.argv:
#         loadData(arg)
