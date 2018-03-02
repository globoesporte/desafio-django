from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Survey, Option
from .serializer import SurveySerializer, OptionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class SurveyPrivate(APIView):
    # Usando o BasicAuthentication para fazer a autenticação sem entrar em mais detalhes.
    # Para usar esse código em produção, recomenda-se usar a autenticação via token
    # Se quiser mesmo usar a BasicAuthentication em produção, ao menos utilize HTTPS
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializerClass = SurveySerializer

    def get(self, request, pk):
        """
        Retorna todas as enquetes caso não tenha passado um PK ou retorna uma enquete específica caso tenha passado um PK
        :param request:
        :param pk:
        :exception ObjectDoesNotExist
        :return:
        """
        if pk:
            try:
                serializer = self.serializerClass(Survey.objects.get(pk=pk))
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = self.serializerClass(Survey.objects.all(), many=True)

        # serializer = self.serializerClass(Survey.objects.get(pk=pk))
        return Response(serializer.data)

    def post(self, request, pk):
        """
        Cria uma nova enquete. Exemplo de enquete criada
        {
            "name": "Qual sua comida favorita?",
            "description": "Escolha sua comida favorita",
            "options": [
                {
                    "description": "Coxinha",
                    "position": 1
                },
                {
                    "description": "Pizza",
                    "position": 2
                }
            ]

        }
        :param request:
        :return:
        """
        serializer = self.serializerClass(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

    def put(self, request, pk):
        """
        Atualiza os dados de uma nova enquete
        url: http://localhost:8000/survey/<id da enquete>
        {
            "name" : "Lista de sex symbols",
            "description": "soh coisa linda de deus"
        }
        :param request:
        :param pk:
        :return:
        """
        # Tem que colocar o partial = true senão ele tenta validar todos os campos,
        # campos obrigatórios que não foram passados como parametros irão disparar exceções
        try:
            survey = Survey.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializerClass(survey, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # você pode passar serializer.data como parametro no response para exibir o objeto criado
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

    def delete(self, request, pk):
        """
        Deleta uma enquete
        :param request:
        :param pk:
        :exception ObjectDoesNotExist
        :exception RuntimeError
        :return:
        """
        try:
            survey = Survey.objects.get(pk=pk)
            survey.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except RuntimeError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OptionPublic(APIView):
    serializerClass = OptionSerializer

    def post(self, request):
        """
        Adiciona um unico voto para uma unica opção
        exemplo de requição:
        url:http://localhost:8000/option/
        body:
        {
            "pk": 999
        }
        onde "pk" é o id da opção
        :
        :param request:
        :return:
        """
        try:
            pk = request.data["id"]
            option = Option.objects.get(pk=pk)
            option.add_vote()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except RuntimeError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OptionPrivate(APIView):
    # Usando o BasicAuthentication para fazer a autenticação sem entrar em mais detalhes.
    # Para usar esse código em produção, recomenda-se usar a autenticação via token
    # Se quiser mesmo usar a BasicAuthentication em produção, ao menos utilize HTTPS
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializerClass = OptionSerializer

    # def put(self,request):
