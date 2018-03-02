# -*- coding: utf-8 -*-
from django.contrib import admin
from polls.models import Option, Vote, Poll


class OptionAdmin(admin.ModelAdmin):
    list_display = ('text', 'display_image','poll',)
    list_filter = ('poll__title',)
    search_fields = ['text', 'poll__title']

    def display_image(self, obj):
        if obj.image:
            return '<img src="%s" width="200px"/>' % obj.image.url

        return '---'
    
    display_image.allow_tags = True


class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'text','vote_count')
    search_fields = ['title']

    def vote_count(self, obj):
        return obj.votes_poll.all().count()


class VoteAdmin(admin.ModelAdmin):
    list_display = ('poll', 'options')
    list_filter = ('poll__title',)
    search_fields = ['poll__title']


admin.site.register(Option, OptionAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(Poll, PollAdmin)

