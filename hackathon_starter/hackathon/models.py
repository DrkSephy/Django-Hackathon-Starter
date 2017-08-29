import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Profile(models.Model):
    user = models.ForeignKey(User)
    oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)


class GithubProfile(models.Model):
    user = models.ForeignKey(User)
    github_user = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    scopes = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)


class TumblrProfile(models.Model):
    user = models.ForeignKey(User)
    tumblr_user = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    access_token_secret = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)


class InstagramProfile(models.Model):
    user = models.ForeignKey(User)
    instagram_user = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)


class TwitterProfile(models.Model):
    user = models.ForeignKey(User)
    twitter_user = models.CharField(max_length=200)
    oauth_token = models.CharField(max_length=200)
    oauth_token_secret = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)


class LinkedinProfile(models.Model):
    user = models.ForeignKey(User)
    linkedin_user = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)


class MeetupToken(models.Model):
    # user = models.ForeignKey(User)
    access_token = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.access_token)


class FacebookProfile(models.Model):
    user = models.ForeignKey(User)
    fb_user_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    profile_url = models.CharField(max_length=50)
    access_token = models.CharField(max_length=100)


class GoogleProfile(models.Model):
    user = models.ForeignKey(User)
    google_user_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    access_token = models.CharField(max_length=100)
    profile_url = models.CharField(max_length=100)


class DropboxProfile(models.Model):
    user = models.ForeignKey(User)
    dropbox_user_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    access_token = models.CharField(max_length=100)


class FoursquareProfile(models.Model):
    user = models.ForeignKey(User)
    foursquare_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    access_token = models.CharField(max_length=100)


class PhotoRequest(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    department_choices = (
        ('News', 'News'),
        ('Sports', 'Sports'),
        ('Opinion', 'Opinion'),
        ('Life', 'Life'),
        ('A&E', 'A&E'),
        ('Focus', 'Focus'),
        ('H&S', 'H&S'),
        ('Video', 'Video'),
        ('Social Media', 'Social Media'),
        ('Humor', 'Humor'),
        ('Gaphics', 'Graphics'),
        ('Photography', 'Photography'),
        ('Advertising', 'Advertising'),
        ('Business', 'Business & Marketing')
    )
    department = models.CharField(max_length=25, choices=department_choices, default='News', blank=False)
    event = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200, blank=False)
    start_date_time = models.DateTimeField(default=datetime.datetime.now, blank=False)
    end_date_time = models.DateTimeField(default=datetime.datetime.now, blank=False)
    submit_date = models.DateTimeField(default=datetime.datetime.now, blank=False)

    def insert(self, fields_dict):
        for field in fields_dict.keys():
            if field.upper() == "department".upper():
                self.department = fields_dict[field]
            elif field.upper() == "event".upper():
                self.event = fields_dict[field]
            elif field.upper() == "description".upper():
                self.description = fields_dict[field]
            elif field.upper() == "first_name".upper():
                self.first_name = fields_dict[field]
            elif field.upper() == "last_name".upper():
                self.last_name = fields_dict[field]
            elif field.upper() == "start_date_time".upper():
                if "/" not in fields_dict[field]:
                    self.start_date_time = fields_dict[field]
                else:
                    start_time = fields_dict[field]
                    start_date = start_time.split(" ")[0]
                    start_time = start_time.split(" ")[1]
                    start_date = start_date.replace("/", "-")
                    self.start_date_time = start_date + " " + start_time
            elif field.upper() == "end_date_time".upper():
                if "/" not in fields_dict[field]:
                    self.end_date_time = fields_dict[field]
                else:
                    end_time = fields_dict[field]
                    end_date = end_time.split(" ")[0]
                    end_time = end_time.split(" ")[1]
                    end_date = end_date.replace("/", "-")
                    self.end_date_time = end_date + " " + end_time
