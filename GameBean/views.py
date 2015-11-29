from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Company, Platform, Game, Review, Genre


def home(request):
    return render(request, "GameBean/index.html", {})

def gamesIndex(request):
    games = Game.objects.order_by('id',)

    paginator_obj = Paginator(games, 50) # show 50 developers at a time
    page = request.GET.get('page')
    try:
        paginator = paginator_obj.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginator = paginator_obj.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginator = paginator_obj.page(paginator.num_pages)

    context = { 'paginator' : paginator,}
    return render(request, "GameBean/games.html", context)

def gameDetail(request, game_name):
    game = get_object_or_404(Game, name=game_name)
    return render(request, 'GameBean/game_detail.html', {'game': game})

def genresIndex(request):
    genres = Genre.objects.order_by('id',)
    paginator_obj = Paginator(genres, 50) # show 50 developers at a time
    page = request.GET.get('page')
    try:
        paginator = paginator_obj.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginator = paginator_obj.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginator = paginator_obj.page(paginator.num_pages)

    context = { 'paginator' : paginator,}
    return render(request, 'GameBean/genres.html', context)

def genreDetail(request, genre_name):
    genre = get_object_or_404(Genre, name=genre_name)
    games = Game.objects.filter(genres=genre).order_by('id',)

    paginator_obj = Paginator(games, 50)
    page = request.GET.get('page')

    try:
        paginator = paginator_obj.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginator = paginator_obj.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginator = paginator_obj.page(paginator.num_pages)

    context = { 'detail_item' : genre, 'paginator' : paginator,}
    return render(request, 'GameBean/genre_detail.html', context)

def developersIndex(request):
    developer_list = Company.objects.order_by('name',)
    paginator_obj = Paginator(developer_list, 50) # show 50 developers at a time
    page = request.GET.get('page')
    try:
        paginator = paginator_obj.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginator = paginator_obj.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginator = paginator_obj.page(paginator.num_pages)

    context = { 'paginator' : paginator,}
    return render(request, 'GameBean/developers.html', context)

def developerDetail(request, developer_name):
    developer = get_object_or_404(Company, name=developer_name)
    games = Game.objects.filter(developers=developer).order_by('id',)
    paginator_obj = Paginator(games, 50)
    page = request.GET.get('page')

    try:
        paginator = paginator_obj.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginator = paginator_obj.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginator = paginator_obj.page(paginator.num_pages)

    context = { 'detail_item' : developer, 'paginator' : paginator,}
    return render(request, "GameBean/developer_detail.html", context)


def platformsIndex(request):
    platform_list = Platform.objects.order_by('id',)
    paginator_obj = Paginator(platform_list, 50) # show 50 developers at a time
    page = request.GET.get('page')
    try:
        paginator = paginator_obj.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginator = paginator_obj.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginator = paginator_obj.page(paginator.num_pages)

    context = { 'paginator' : paginator,}
    return render(request, 'GameBean/platforms.html', context)

def platformDetail(request, platform_name):
    platform = get_object_or_404(Platform, name=platform_name)
    games = Game.objects.filter(platforms=platform).order_by('id',)
    paginator_obj = Paginator(games, 50)
    page = request.GET.get('page')

    try:
        paginator = paginator_obj.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginator = paginator_obj.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginator = paginator_obj.page(paginator.num_pages)

    context = { 'detail_item' : platform, 'paginator' : paginator,}
    return render(request, "GameBean/developer_detail.html", context)
