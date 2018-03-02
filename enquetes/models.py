from django.db import models, transaction


class Enquete(models.Model):
    texto = models.CharField(max_length=250)
    ativa = models.BooleanField()

    def __str__(self):
        return self.texto


class Resposta(models.Model):
    enquete = models.ForeignKey(
        Enquete, on_delete=models.CASCADE, related_name='respostas',)
    opcao = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    @classmethod
    def votar(cls, id):
        '''
            Método para controle de concorrência na votação.
        '''
        with transaction.atomic():
            resposta = (
                cls.objects
                .select_for_update()
                .get(id=id)
            )
        resposta.votos += 1
        resposta.save()

        resposta.save()

        return resposta

    def __str__(self):
        return self.opcao
