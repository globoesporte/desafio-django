from django.db import models

class Question(models.Model):
    readonly_fields = ['pub_date']
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(
        verbose_name='date published', auto_now=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    readonly_fields = ['pub_date']
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(
        verbose_name='date published', auto_now=True)

    def __str__(self):
        return self.choice_text

    def add_vote(self):
        self.votes += 1
        self.save()

