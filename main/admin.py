from django.contrib import admin
from main.models import Zombie, Tweet


class ZombieAdmin(admin.ModelAdmin):
    list_display = ('name', 'cementery',)


class TweetAdmin(admin.ModelAdmin):
    list_display = ('zombie', 'status')
    search_fields = ('zombie',)


admin.site.register(Zombie, ZombieAdmin)
admin.site.register(Tweet, TweetAdmin)
