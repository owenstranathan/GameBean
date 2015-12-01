from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain

import logging
logger = logging.getLogger(__name__)

from .models import Company, Platform, Game, Review, Genre

from .forms import SearchForm, ReviewForm

from .utils import get_query


def home(request):
    form = SearchForm()
    return render(request, "GameBean/index.html", {'form' : form})

def gamesIndex(request):
    games = Game.objects.order_by('id',)
    form = SearchForm()
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

    context = { 'paginator' : paginator,
                'form' : form, }

    return render(request, "GameBean/games.html", context)

def gameDetail(request, game_name):

    form = SearchForm()
    game = get_object_or_404(Game, name=game_name)
    reviewForm = ReviewForm()

    if request.method == 'POST':
        reviewForm = ReviewForm(request.POST)
        if reviewForm.is_valid():
            topic = reviewForm.cleaned_data["topic"]
            text = reviewForm.cleaned_data["text"]
            review = Review(topic=topic, text=text, game=game)
            review.save()

    reviews = Review.objects.filter(game=game)
    context = {'game': game,
               'form' : form,
               'reviewForm' : reviewForm,
               'reviews' : reviews, }
    return render(request, 'GameBean/game_detail.html', context )

def genresIndex(request):
    genres = Genre.objects.order_by('id',)
    form = SearchForm()
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

    context = { 'paginator' : paginator,
                'form' : form,}

    return render(request, 'GameBean/genres.html', context)

def genreDetail(request, genre_name):
    genre = get_object_or_404(Genre, name=genre_name)
    games = Game.objects.filter(genres=genre).order_by('id',)
    form = SearchForm()

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

    context = { 'detail_item' : genre,
                'paginator' : paginator,
                'form' : form,}

    return render(request, 'GameBean/genre_detail.html', context)

def developersIndex(request):
    developer_list = Company.objects.order_by('name',)
    form = SearchForm()
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

    context = { 'paginator' : paginator,
                'form' : form,}

    return render(request, 'GameBean/developers.html', context)

def developerDetail(request, developer_name):
    developer = get_object_or_404(Company, name=developer_name)
    games = Game.objects.filter(developers=developer).order_by('id',)
    form = SearchForm()
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

    context = { 'detail_item' : developer,
                'paginator' : paginator,
                'form' : form,}

    return render(request, "GameBean/developer_detail.html", context)


def platformsIndex(request):
    platform_list = Platform.objects.order_by('id',)
    form = SearchForm()
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

    context = { 'paginator' : paginator,
                'form' : form,}

    return render(request, 'GameBean/platforms.html', context)

def platformDetail(request, platform_name):
    platform = get_object_or_404(Platform, name=platform_name)
    games = Game.objects.filter(platforms=platform).order_by('id',)
    form = SearchForm()
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

    context = { 'detail_item' : platform,
                'paginator' : paginator,
                'form' : form,}
    return render(request, "GameBean/developer_detail.html", context)

def search(request):
    searchTerms = None
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            searchTerms = form.cleaned_data['searchWord']
        else:
            raise Http404

    elif request.method == 'GET':
        if request.COOKIES.has_key('searchTerms'):
            searchTerms = request.COOKIES['searchTerms']
        else:
            raise Http404

    found_entries = None
    entry_query = get_query(searchTerms, ['name', 'description', ])
    game_results = Game.objects.filter(entry_query).order_by('name')
    platform_results = Platform.objects.filter(entry_query).order_by('name')
    company_results = Company.objects.filter(entry_query).order_by('name')
    genre_results = Genre.objects.filter(entry_query).order_by('name')

    found_entries = list(chain(game_results, company_results, platform_results, genre_results))

    paginator_obj = Paginator(found_entries, 100) # show 50 items at a time

    page = request.GET.get('page')
    try:
        paginator = paginator_obj.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginator = paginator_obj.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginator = paginator_obj.page(paginator.num_pages)

    context = { 'paginator' : paginator,
                'searchTerms': searchTerms,
                'number_of_entries': len(found_entries),
                'form' : form, }

    response = render(request, 'GameBean/search_results.html', context)
    response.set_cookie('searchTerms', searchTerms)
    return response
