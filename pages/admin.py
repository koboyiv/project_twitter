from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.twitter_ac)
admin.site.register(models.cal_tweets)
admin.site.register(models.data_twitter)

