from django.contrib import admin
from .models import Question
from .models import Choice


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['question_text']
    search_fields = ['question_text', 'pub_date']

class ChoiceAdmin(admin.ModelAdmin):
    list_filter = ['question']
    search_fields = ['question_text', 'votes']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
