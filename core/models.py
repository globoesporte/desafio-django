from django.db import models, transaction


class Survey(models.Model):
    active = models.BooleanField()
    description = models.CharField(max_length=300)
    def __str__(self):
        return self.description


class Options(models.Model):
    survey = models.ForeignKey(Survey, 
                               on_delete=models.CASCADE,
                               related_name='options')
    votes = models.IntegerField(default=0)
    option = models.CharField(max_length=300)

    @classmethod
    def vote(cls, id,number):
        with transaction.atomic():
            option = (cls.objects.select_for_update().get(id=id))
        option.votes += number
        option.save()
        return option

    def __str__(self):
        return self.option
