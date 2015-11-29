from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^Games/$', views.gamesIndex, name='games'),
    url(r'^Games/(?P<game_name>.+)/$', views.gameDetail, name='game_detail'),
    url(r'^Genres/$', views.genresIndex, name='genres'),
    url(r'^Genres/(?P<genre_name>.+)/$', views.genreDetail, name='genre_detail'),
    url(r'^Developers/$', views.developersIndex, name='developers'),
    url(r'^Developers/(?P<developer_name>.+)/$', views.developerDetail, name='developer_detail'),
    url(r'^Platforms/$', views.platformsIndex, name='platforms'),
    url(r'^Platforms/(?P<platform_name>.+)/$', views.platformDetail, name='platform_detail'),
    url(r'^Search/$', views.search, name='search'),
]
