# Desafio GloboEsporte

## Instruções para rodar

* cd src
* sudo docker-compose up --build

## Acessando django template

    0.0.0.0:8000/enqueteapp

## API
* All Questions
    * 0.0.0.0:8000/api
* Question
    * 0.0.0.0:8000/api/id_questao ( id_questao = id numérico de uma questão cadastrada )
* All Choices
    * 0.0.0.0:8000/api/choices
* Choices
    * 0.0.0.0:8000/api/choices/id_escolha ( id_escolha = id numérico de uma escolha cadastrada )
* Vote
    * 0.0.0.0:8000/api/vote/id_escolha ( id_escolha = id numérico de uma escolha cadastrada )
