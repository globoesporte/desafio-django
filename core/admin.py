from django.contrib import admin
from .models import Survey, Options


# admin.site.register(Option)


class SurveyAdmin(admin.ModelAdmin):
    search_fields = ('description',)


class OptionAdmin(admin.ModelAdmin):
    search_fields = ('description',)


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Options, OptionAdmin)
