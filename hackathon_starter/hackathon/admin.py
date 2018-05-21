# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from hackathon.models import (UserProfile, Profile, InstagramProfile,
                              TwitterProfile, MeetupToken, GithubProfile,
                              LinkedinProfile, TumblrProfile)
from hijack_admin.admin import HijackRelatedAdminMixin


# include hijack
class TwitterProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'twitter_user')


class UserAdmin(HijackRelatedAdminMixin, admin.ModelAdmin):
    list_display = ('user', 'hijack_field')


admin.site.register(UserProfile, UserAdmin)
admin.site.register(Profile)
admin.site.register(InstagramProfile)
admin.site.register(TwitterProfile, TwitterProfileAdmin)
admin.site.register(GithubProfile)
admin.site.register(MeetupToken)
admin.site.register(LinkedinProfile)
admin.site.register(TumblrProfile)
