from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^Games/$', views.gamesIndex, name='games'),
    url(r'^Games/(?P<game_name>.+)/$', views.gameDetail, name='game_detail'),
    url(r'^Games/(?P<game_name>.+)/\?update_review_from=(?P<reviewer_name>.+)$', views.updateReview, name='review_update'),
    url(r'^Genres/$', views.genresIndex, name='genres'),
    url(r'^Genres/(?P<genre_name>.+)/$', views.genreDetail, name='genre_detail'),
    url(r'^Developers/$', views.developersIndex, name='developers'),
    url(r'^Developers/(?P<developer_name>.+)/$', views.developerDetail, name='developer_detail'),
    url(r'^Platforms/$', views.platformsIndex, name='platforms'),
    url(r'^Platforms/(?P<platform_name>.+)/$', views.platformDetail, name='platform_detail'),
    url(r'^Search/$', views.search, name='search'),
    url(r'^Login/$', views.login, name='login'),
    url(r'^Logout/$', views.logout, name='logout'),
    url(r'^SignUp/$', views.signUp, name='sign_up'),
    url(r'^User/(?P<username>.+)/$', views.profile, name='profile'),
    url(r'^About/$', views.about, name='about'),
    url(r'^Delete/Review/(?P<game_name>.+)/(?P<reviewer_name>.+)/$', views.deleteReview, name='review_delete'),
    url(r'^Update/Review/(?P<game_name>.+)/(?P<reviewer_name>.+)/$', views.updateReview, name='review_update'),
    url(r'^Vote/', views.vote, name='vote'),

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
