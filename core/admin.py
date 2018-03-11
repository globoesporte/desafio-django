from django.contrib import admin
from .models import Survey, Options
from django.db.models import Q
from django.db.models import Sum


class InputFilter(admin.SimpleListFilter):
    template = 'admin/input_filter.html'

    def lookups(self, request, model_admin):
        return ((),)

    def choices(self, changelist):
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )


        yield all_choice

class OptionFilter(InputFilter):
    parameter_name = 'description'
    title = ('Description')

    def queryset(self, request, queryset):
        term = self.value()

        if term is None:
            return

        any_name = Q()
        for bit in term.split():
            any_name &= (
                Q(option__icontains=bit)
            )

        return queryset.filter(any_name)


class SurveyFilter(InputFilter):
    parameter_name = 'description'
    title = ('Description')

    def queryset(self, request, queryset):
        term = self.value()

        if term is None:
            return

        any_name = Q()
        for bit in term.split():
            any_name &= (
                Q(description__icontains=bit)
            )

        return queryset.filter(any_name)

class OptionInline(admin.StackedInline):
    model = Options



class SurveyAdmin(admin.ModelAdmin):
    list_display = ('description','active','options','votes')
    list_filter = (SurveyFilter,'active')
    search_fields = ['description',]
    inlines = [
        OptionInline,
    ]
    def votes(self, obj):
        return obj.options.aggregate(Sum('votes'))['votes__sum']


class OptionAdmin(admin.ModelAdmin):
    list_display = ('option','votes',)
    list_filter = (OptionFilter,)
    search_fields = ['description',]


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Options, OptionAdmin)
