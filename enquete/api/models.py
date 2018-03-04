from django.db import models
import uuid
from django.utils.timezone import now

# Create your models here.
class Enquete(models.Model):
    id =  models.AutoField(primary_key=True)
    uuid =  models.UUIDField(default=uuid.uuid4, editable=False, null=False)
    nome = models.CharField(max_length=60, blank=False, null=False)
    descricao = models.CharField(max_length=500, blank=False, null=False)
    data_criacao = models.DateTimeField(default=now, editable=False,  blank=False, null=False)

    class JSONAPIMeta:
        resource_name = "enquetes"

    # def __str__(self):
    #     return 

    # def __unicode__(self):
    #     return 

class Item(models.Model):
    id =  models.AutoField(primary_key=True)
    uuid =  models.UUIDField(default=uuid.uuid4, editable=False, blank=False, null=False)
    nome = models.CharField(max_length=60, blank=False, null=False)
    valor = models.CharField(max_length=20, blank=False, null=False)
    descricao = models.CharField(max_length=500, blank=False, null=False)
    enquete = models.ForeignKey(Enquete, on_delete=models.CASCADE, related_name="itens")
    data_criacao = models.DateTimeField(default=now, editable=False, blank=False, null=False)

    class JSONAPIMeta:
        resource_name = "itens"

    # def __str__(self):
    #     return 

    # def __unicode__(self):
    #     return 

class Voto(models.Model):
    id =  models.AutoField(primary_key=True)
    uuid =  models.UUIDField(default=uuid.uuid4, editable=False, blank=False, null=False)
    enquete = models.ForeignKey(Enquete, on_delete=models.CASCADE, null=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False)
    data_criacao = models.DateTimeField(default=now, editable=False, blank=False, null=False)

    def __str__(self):
        return 

    def __unicode__(self):
        return 
