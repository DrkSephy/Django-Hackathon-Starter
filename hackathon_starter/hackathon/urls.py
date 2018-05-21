from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from hackathon import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^register/?$', views.register, name='register'),
    url(r'^login/?$', views.user_login, name='login'),
    url(r'^logout/?$', views.user_logout, name='logout'),
    url(r'^api/?$', views.api_examples, name='api'),
    url(r'^steam/?$', views.steam, name='steam'),
    url(r'^steamDiscountedGames/?$', views.steamDiscountedGames, name='steamDiscountedGames'),
    url(r'^githubResume/?$', views.githubResume, name='githubResume'),
    url(r'^githubUser/?$', views.githubUser, name='githubUser'),
    url(r'^githubTopRepositories/?$', views.githubTopRepositories, name='githubTopRepositories'),
    url(r'^tumblr/?$', views.tumblr, name='tumblr'),
    url(r'^linkedin/?$', views.linkedin, name='linkedin'),
    url(r'^twilio/?$', views.twilio, name='twilio'),
    url(r'^instagram/?$', views.instagram, name='instagram'),
    url(r'^instagram_login/?$', views.instagram_login, name='instagram_login'),
    url(r'^instagramUser/?$', views.instagramUser, name='instagramUser'),
    url(r'^instagramMediaByLocation/?$', views.instagramMediaByLocation, name='instagramMediaByLocation'),  #
    url(r'^instagramUserMedia/?$', views.instagramUserMedia, name='instagramUserMedia'),
    url(r'^twitter/?$', views.twitter, name='twitter'),
    url(r'^twitterTweets/?$', views.twitterTweets, name='twitterTweets'),
    url(r'^tumblr_login/?$', views.tumblr_login, name='tumblr_login'),
    url(r'^twitter_login/?$', views.twitter_login, name='twitter_login'),
    url(r'^github_login/?$', views.github_login, name='github_login'),
    url(r'^linkedin_login/?$', views.linkedin_login, name='linkedin_login'),
    url(r'^facebook_login/?$', views.facebook_login, name='facebook_login'),
    url(r'^facebook/?$', views.facebook, name='facebook'),
    url(r'^google_login/?$', views.google_login, name='google_login'),
    url(r'^google/?$', views.googlePlus, name='googlePlus'),
    url(r'^dropbox_login/?$', views.dropbox_login, name='dropbox_login'),
    url(r'^dropbox/?$', views.dropbox, name='dropbox'),
    url(r'^dropboxSearchFile/?$', views.dropboxSearchFile, name='dropboxSearchFile'),
    url(r'^foursquare_login/?$', views.foursquare_login, name='foursquare_login'),
    url(r'^foursquare/?$', views.foursquare, name='foursquare'),
    url(r'^quandlSnp500/?$', views.quandlSnp500, name='quandlsnp500'),
    url(r'^quandlNasdaq/?$', views.quandlNasdaq, name='quandlnasdaq'),
    url(r'^quandlNasdaqdiff/?$', views.quandlNasdaqdiff, name='quandlnasdaqdiff'),
    url(r'^quandlDowJones/?$', views.quandlDowJones, name='quandldowjones'),
    url(r'^quandlstocks/?$', views.quandlstocks, name='quandlstocks'),
    url(r'^quandlapple/?$', views.quandlapple, name='quandlapple'),
    url(r'^quandlapplediff/?$', views.quandlapplediff, name='quandlapplediff'),
    url(r'^quandlDowJonesdiff/?$', views.quandlDowJonesdiff, name='quandldowjonesdiff'),
    url(r'^quandlSnp500diff/?$', views.quandlSnp500diff, name='quandlsnp500diff'),
    url(r'^nytimespop/?$', views.nytimespop, name='nytimespop'),
    url(r'^nytimestop/?$', views.nytimestop, name='nytimestop'),
    url(r'^nytimesarticles/?$', views.nytimesarticles, name='nytimesarticles'),
    url(r'^meetup/?$', views.meetup, name='meetup'),
    url(r'^meetupToken/?$', views.meetupToken, name='meetupToken'),
    url(r'^meetupUser/?$', views.meetupUser, name='meetupUser'),
    url(r'^yelp/?$', views.yelp, name='yelp'),
]
