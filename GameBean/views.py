"""USER AUTHENTICATION"""
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User
from .forms import LoginForm, SignUpForm

"""USER PROFILES"""
from .models import GameSprout
from .forms import ProfileImageForm

"""Response"""
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404

"""PAGINATION"""
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain

"""LOGGING"""
import logging
logger = logging.getLogger(__name__)

"""GAMEBEAN"""
from .models import Company, Platform, Game, Genre
from .forms import ReviewForm

"""REVIEWING"""
from .models import Review#, ReviewVoter

"""REVIEW VOTING """
from django.views.decorators.csrf import ensure_csrf_cookie


"""GAME VOTING"""
# from .models import GameVoter

"""SEARCHING"""
from .forms import SearchForm
from .utils import get_query

"""MESSAGING"""
from django.contrib import messages
from django.contrib.messages import get_messages

def home(request):
    form = SearchForm()
    top_reviews = Review.objects.all().order_by('-publish_date')[:4]
    return render(request, "GameBean/index.html", {'form' : form, 'user':request.user, 'reviews' : top_reviews, })

def login(request):
    form = SearchForm()
    has_error = False
    error = ""
    if request.method == 'GET':
        loginForm = LoginForm()
        # return render(request, "GameBean/login.html", context)
    elif request.method == 'POST':
        # construct login from
        loginForm = LoginForm(request.POST)
        # validate form
        if loginForm.is_valid():
            # get form fields
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']

            # authenticate user
            user = authenticate(username=username, password=password)

            # if the user is authenticated
            if user is not None:
                # login the user (uses session/provided by django)
                django_login(request, user)
                #redirect to home
                messages.add_message(request, messages.INFO, "<strong>Login Successful!</strong> Welcome " + user.username,  extra_tags="alert alert-success fade in")
                return redirect('home')
            # if authentication fails
            else:
                # figure out why
                has_error = True
                try:
                    user = User.objects.get(username=username)
                    #invalid password
                    if user is not None:
                        error = "Invalid Password for username " + username
                #invalid username
                except User.DoesNotExist:
                    error = "User for username " + username + " not found."
        else:
            # fail because of incomplete form
            has_error = True
            error = "Login form must be filled correctly"

    context = {'form': form, 'loginForm' : loginForm, 'has_error': has_error, 'error' : error}

    return render(request, "GameBean/login.html", context)

def logout(request):
    django_logout(request)
    return redirect('home')

def signUp(request):
    form = SearchForm()
    has_error = False
    error = ""
    if request.method == 'GET':
        signUpForm = SignUpForm()

    elif request.method == 'POST':
        signUpForm = SignUpForm(request.POST)
        if signUpForm.is_valid():
            email = signUpForm.cleaned_data["email"]
            username = signUpForm.cleaned_data["username"]
            password = signUpForm.cleaned_data["password"]
            confirmation_password = signUpForm.cleaned_data["confirmation_password"]
            if confirmation_password != password:
                has_error = True
                error = "confirmation password and password differ, please ensure they are the same"
            else:
                try:
                    # this will fail if the user is not in the database
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    user = User.objects.create_user(username, email=email, password=password)
                    user = authenticate(username=username, password=password)
                    django_login(request, user)
                    game_sprout = GameSprout(user=user)
                    game_sprout.save()
                    messages.add_message(request, messages.INFO, '<strong>Profile <span style="color:#33cc33">' + username + '</span> created successfully!</strong> Welcome to GameBean!',  extra_tags="alert alert-success fade in")
                    return redirect('home')

                has_error = True
                error = "User with username " + username + " already exists, please try another name."



    context = { 'form' : form, 'signUpForm' : signUpForm, 'has_error': has_error, 'error' : error}
    return render(request, "GameBean/sign_up.html", context)

def profile(request, username):
    if request.method == 'POST':
        imageForm = ProfileImageForm(request.POST)
        if imageForm.is_valid():
            image = imageForm.cleaned_data["image"]
            user = User.objects.get(username=username)
            game_sprout = GameSprout.objects.get(user=user)
            game_sprout.image = image
            game_sprout.save()
            messages.succes(request, "<strong>Profile image updated!</strong> congratulations, you interneted!", extra_tags="alert alert-success fade in")

    imageForm = ProfileImageForm()
    has_reviews = True
    reviews = []
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        messages.add_message(request, messages.INFO, "<strong>Sorry duder</strong> that user couldn't be found, you probably typed it wrong... yeah that's what it is, it's your fault. Contact admin if your sure you're right. Buy you're probably wrong. Just sayin'", extra_tags="alert alert-warning fade in")
        redirect('home')
    try:
        game_sprout = GameSprout.objects.get(user=user)
    except GameSprout.DoesNotExist:
        messages.add_message(request, messages.INFO, "<strong>Sorry duder</strong> that user couldn't be found, weird... If this keeps happening erroneously contact admin.", extra_tags="alert alert-warning fade in")
        redirect('home')

    # get user's reviews
    reviews = Review.objects.filter(reviewer=user).order_by('publish_date',)
    # if there are no reviews set flag so message can be diplayed
    if not reviews:
        has_reviews = False

    form = SearchForm()

    context = {
        'form' : form,
        'user' : request.user,
        'profile_user' : user,
        'game_sprout' : game_sprout,
        'has_reviews' : has_reviews,
        'reviews' : reviews,
        'imageForm' : imageForm,
    }

    return render(request, "GameBean/profile.html", context)


def gamesIndex(request):
    games = Game.objects.exclude(release_date=None).order_by('-release_date',)
    games = list(games)
    games.append(list(Game.objects.filter(release_date=None)))
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
                'form' : form,
                'user':request.user,
                'num_games' : len(games)
                }

    return render(request, "GameBean/games.html", context)



# updateReview should equal the id of the review to update
def gameDetail(request, game_name):
    print "DETAIL"
    form = SearchForm()
    game = get_object_or_404(Game, name=game_name)
    reviewForm = ReviewForm()
    user_has_reviewed = False


    try:
        review = Review.objects.get(reviewer=request.user, game=game)
        user_has_reviewed = True
    except:
        print "User hasn't reviewed"

    if request.method == 'POST':
        reviewForm = ReviewForm(request.POST)
        if reviewForm.is_valid():
            try:
                review = Review.objects.get(reviewer=request.user, game=game)
                messages.add_message(request, messages.INFO, "<strong>WHOA THERE BUSTER!</strong> You gotta be more careful when your resending data, you almost put a duplicate entry in our database. Thats not cool!", extra_tags="alert alert-warning fade in")
                return redirect('game_detail', game_name=game_name)
            except:
                title = reviewForm.cleaned_data["title"]
                text = reviewForm.cleaned_data["text"]
                review = Review(title=title, text=text, reviewer=request.user, game=game)
                review.save()

    reviews = Review.objects.filter(game=game)
    context = {'game': game,
               'form' : form,
               'reviewForm' : reviewForm,
               'reviews' : reviews,
               'user': request.user,
               'user_has_reviewed' : user_has_reviewed,
               }
    return render(request, 'GameBean/game_detail.html', context )


def deleteReview(request, reviewer_name, game_name):
    print game_name
    game = get_object_or_404(Game, name=game_name)
    user = User.objects.get(username=reviewer_name)
    try:
        review = Review.objects.get(reviewer=user, game=game)
        review.delete()
    except Review.DoesNotExist:
        pass

    return redirect('game_detail', game_name=game_name)

def updateReview(request, game_name, reviewer_name):
    print "UPDATE"
    form = SearchForm()
    game = get_object_or_404(Game, name=game_name)
    reviewForm = ReviewForm()
    user = User.objects.get(username=reviewer_name)
    review = Review.objects.get(reviewer=user, game=game)
    data = { 'title': review.title, 'text' : review.text }
    updateReviewForm = ReviewForm(data=data)

    if request.method == 'POST':
        reviewForm = ReviewForm(request.POST)
        if reviewForm.is_valid():
            review.title = reviewForm.cleaned_data["title"]
            review.text = reviewForm.cleaned_data["text"]
            review.save()
            return HttpResponseRedirect("/GameBean/Games/"+game_name+"/#"+reviewer_name)

    reviews = Review.objects.filter(game=game)
    context = {
               'game': game,
               'form' : form,
               'reviewForm' : reviewForm,
               'update' : True,
               'updateReviewForm' : updateReviewForm,
               'reviews' : reviews,
               'user': request.user,
               }
    return render(request, 'GameBean/game_detail.html', context )

@ensure_csrf_cookie
def vote(request):
    print "VOTE"
    print request.POST

    review_id = int(request.POST['id'])
    print 1
    vote_type = request.POST['type']
    print 2
    vote_action = request.POST['action']
    print 3


    review = get_object_or_404(Review, pk=review_id)
    print 4


    user_up_voted = review.upVotes.filter(id = request.user.id).count()
    print 5
    user_down_voted = review.downVotes.filter(id = request.user.id).count()

    if (vote_action == 'vote'):
        if (user_up_voted == 0) and (user_down_voted == 0):
            if (vote_type == 'up'):
                review.upVotes.add(request.user)
            elif (vote_type == 'down'):
                review.downVotes.add(request.user)
            else:
                return HttpResponse('error-unknown vote type')
        else:
            return HttpResponse('error - already voted', user_up_voted, user_down_voted)
    elif (vote_action == 'recall-vote'):
        if (vote_type == 'up') and (user_up_voted == 1):
            review.upVotes.remove(request.user)
        elif (vote_type == 'down') and (user_down_voted ==1):
            review.downVotes.remove(request.user)
        else:
            return HttpResponse('error - unknown vote type or no vote to recall')
    else:
        return HttpResponse('error - bad action')


    num_votes = review.upVotes.count() - review.downVotes.count()

    return HttpResponse(num_votes)




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
                'form' : form,
                'user':request.user,
                }

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
                'form' : form,
                'user':request.user,
                }

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
                'form' : form,
                'user':request.user,
                }

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
                'form' : form,
                'user':request.user,
                }

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
                'form' : form,
                'user':request.user,
                }

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
                'form' : form,
                'user':request.user,
                }
    return render(request, "GameBean/platform_detail.html", context)

def search(request):
    searchTerms = None
    nothing_found = False
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            searchTerms = form.cleaned_data['searchWord']
        else:
            return render(request, 'GameBean/search_results.html', {'form' : form, 'nothing_found' : True, 'user':request.user,})


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
    for obj in found_entries:
        if searchTerms in obj.name:
            found_entries.remove(obj)
            found_entries.insert(0, obj)

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
                'form' : form,
                'user':request.user,
                }

    response = render(request, 'GameBean/search_results.html', context)
    response.set_cookie('searchTerms', searchTerms)
    return response

def about(request):
    form = SearchForm()
    return render(request, 'GameBean/about.html', { 'form' : form})
