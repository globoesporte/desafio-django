from django.db import models


class Survey(models.Model):
    # Enqute, possui o nome e uma descrição
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Option(models.Model):
    # A opção de cada enquente. Deve possuir a descrição da opção, sua posição, a quantidade de votos e a FK da pesquisa
    description = models.CharField(max_length=30)  # position só serve para ajudar na hora de exibir as opções
    survey = models.ForeignKey(Survey, related_name='options', on_delete=models.CASCADE)
    position = models.IntegerField()
    votes = models.IntegerField(default=0)

    def add_vote(self):
        self.votes += 1
        self.save()

    def __str__(self):
        return "%s - %s " % (self.survey.name, self.description)

    class Meta:
        ordering = ['position']
