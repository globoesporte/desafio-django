from django.db import models


class Survey(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Option(models.Model):
    description = models.CharField(max_length=30)
    survey = models.ForeignKey(Survey, related_name='options', on_delete=models.CASCADE)
    position = models.IntegerField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "%s - %s " % (self.survey.name, self.description)

    class Meta:
        ordering = ['position']
