# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)



class GithubProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    github_user = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    scopes = models.CharField(max_length=200)


class TumblrProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    tumblr_user = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    access_token_secret = models.CharField(max_length=200)


class InstagramProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    instagram_user = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)


class TwitterProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    twitter_user = models.CharField(max_length=200)
    oauth_token = models.CharField(max_length=200)
    oauth_token_secret = models.CharField(max_length=200)


class LinkedinProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    linkedin_user = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

class MeetupToken(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL)
    access_token = models.CharField(max_length=200)


class FacebookProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    fb_user_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    profile_url = models.CharField(max_length=50)
    access_token = models.CharField(max_length=100)


class GoogleProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    google_user_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    access_token = models.CharField(max_length=100)
    profile_url = models.CharField(max_length=100)


class DropboxProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    dropbox_user_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    access_token = models.CharField(max_length=100)


class FoursquareProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    foursquare_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    access_token = models.CharField(max_length=100)
