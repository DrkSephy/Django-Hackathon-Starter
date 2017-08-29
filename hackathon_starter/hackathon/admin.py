from django.contrib import admin
from .models import UserProfile, Profile, InstagramProfile, TwitterProfile, MeetupToken, GithubProfile, LinkedinProfile, TumblrProfile, PhotoRequest

# Register your models here.
class TwitterProfileAdmin(admin.ModelAdmin):
	list_display = ('user','twitter_user')
class PhotoRequestAdmin(admin.ModelAdmin):
	list_display = ('event','first_name', 'last_name', 'department', 'submit_date')
	list_filter = ('submit_date', 'start_date_time', 'department', 'first_name', 'last_name')

admin.site.register(UserProfile)
admin.site.register(Profile)
admin.site.register(PhotoRequest, PhotoRequestAdmin)
