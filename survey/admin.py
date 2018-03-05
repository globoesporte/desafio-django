from django.contrib import admin
from .models import Survey, Option


# admin.site.register(Option)


class SurveyAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class OptionAdmin(admin.ModelAdmin):
    search_fields = ('description',)

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Option, OptionAdmin)
