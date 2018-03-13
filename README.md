# Desafio Python/Django Globoesporte

Esse projeto é uma API em Python 3.6.3 usando Django 2.0.2 e Django Rest Framework 3.7.7 para poder criar, modificar e deletar enquetes. 

# O que foi feito

* Codigo feito em PEP8 e verificado por meio de [autopep8](https://pypi.python.org/pypi/autopep8) 
* API REST com EndPoints POST, GET, PUT e DELETE
* Template na home principal para votação e visualização das enquetes com animações e avisos
* Admin com filtros personalizados e busca  com adição de dados importantes nas paginas. 
* Docker e arquivo com requerimentos
* Testes unitários(totalizando 18) que verificam cada endpoint e a variação de parâmetros possíveis
* Fila de Carga de votos na memória que é descarregada a cada 1 minuto.
* Deploy em pythonanywhere [aqui](http://ldepaulaf.pythonanywhere.com/)


## Instalando no Docker

Rodando o arquivo em Docker:
É muito simples. Primeiramente instale o [Compose](https://docs.docker.com/compose/install/#install-compose) para facilitar ao processo. 

com o composer instalado, basta ir na pasta do projeto e usar os seguintes comandos na mesma pasta onde há o arquivo manage.py
```
docker-compose run web manage.py migrate

docker-compose build

docker-compose up
```
E imediatamente o docker estará funcionando na porta 8000 do localhost


## Acessando no Python Anywhere

Para ver o site em deploy no python anywhere, acesse http://ldepaulaf.pythonanywhere.com/

Para as requisições use o usuário admin e a senha é globoadmin.

## Utilizando task para controle de votos

O site utiliza o [django-background-task](http://django-background-tasks.readthedocs.io/en/latest/) para criar a fila e contabilizar os votos a cada 1 minuto, para roda-lo no pythonanywhere precisa-se ir na aba de consoles e em um console (rodando o devido virtualenv)o seguinte código:
```
 python manage.py process_tasks
 ```

## Endpoints 
Os Endpoints foram planejados para aceitar envios com parâmetros explícitos ou ignorando a chamada do nome dos mesmos

## Endpoints implícito.

* {id} é o id da enquete ou opção/voto 
* O único que não precisa de autenticação é o /vote POST, o PUT e DELETE, decidi manter a segurança, pois são ações de administração e com um futuro login seria possível o usuário mudar seu voto

| Caminho       | Método | Parâmetros | Descrição
| :---          |  :---: |       :---:      | ---: |
| /api/surveys       | POST   |      description, active       | Cria uma enquete |
| /api/surveys       | GET    | N/A              | Recupera as informações de todas as enquetes |
| /api/surveys/{id survey}    | GET    | N/A              | Recupera as informações de uma única enquete|
| /api/surveys/{id survey}   | PUT    | description, active              | Atualiza informações de uma enquete|
| /api/surveys/{id survey}    | DELETE | N/A              | Deleta uma enquete|
| /api/vote/{id survey}/{id voto}          | POST   | N/A              | Vota em uma única enquete|
| /api/vote/{id survey}/{id voto antigo}/{id voto novo}        | PUT   | N/A              | Muda seu voto em uma única enquete|
| /api/vote/{id survey}/{id voto}        | DELETE   | N/A              | Deleta seu voto em uma única enquete|
| /api/options      | POST   |  option, survey              | Cria uma nova opção de enquete|
| /api/options/{id survey}/{id voto}     | PUT    | option              | Atualiza uma opção de enquete|
| /api/options/{id survey}/{id voto}     | DELETE | N/A              | Deleta uma opção de enquete|

## Endpoints explícitos.

* {id} é o id da enquete ou opção/voto 
* O único que não precisa de autenticação é o /vote POST, o PUT e DELETE, decidi manter a segurança, pois são ações de administração e com um futuro login seria possível o usuário mudar seu voto

| Caminho       | Método | Parâmetros | Descrição
| :---          |  :---: |       :---:      | ---: |
| /api/surveys       | POST   |      description, active       | Cria uma enquete |
| /api/surveys       | GET    | N/A              | Recupera as informações de todas as enquetes |
| /api/surveys/survey={id}    | GET    | N/A              | Recupera as informações de uma única enquete|
| /api/surveys/survey={id}   | PUT    | description, active              | Atualiza informações de uma enquete|
| /api/surveys/survey={id}   | DELETE | N/A              | Deleta uma enquete|
| /api/vote/survey={id}/option={id}          | POST   | N/A              | Vota em uma única enquete|
| /api/vote/survey={id}/old_option={id}/new_option={id}        | PUT   | N/A              | Muda seu voto em uma única enquete|
| /api/vote/survey={id}/option={id}          | DELETE   | N/A              | Deleta seu voto em uma única enquete|
| /api/options      | POST   |  option, survey              | Cria uma nova opção de enquete|
| /api/options/survey={id}/option={id}    | PUT    | option              | Atualiza uma opção de enquete|
| /api/options/survey={id}/option={id}    | DELETE | N/A              | Deleta uma opção de enquete|



## Autenticação
Esse projeto utiliza [Basic Access Authetication](https://en.wikipedia.org/wiki/Basic_access_authentication) para fazer a autenticação em todos os endpoints protegidos. Para interagir com esses endpoints, é necessário passar suas credencias no header da chamada. Para facilitar a sua vida, eu recomendo usar o [httpie](https://httpie.org/) (o melhor é feito em python).

## View Django template

O site possui um único template, que mostra todas as enquetes (com uma animação de porcentagem em circulo).  http://ldepaulaf.pythonanywhere.com/surveys/ ou http://ldepaulaf.pythonanywhere.com/ 

## Exemplos de usos
os exemplos a seguir usam httpie e o login basico para testes


```
http --form GET http://ldepaulaf.pythonanywhere.com/api/surveys/ -a admin:globoadmin
```
```

    {
        "active": true,
        "description": "O trabalho está bom?",
        "id": 1,
        "options": [
            {
                "id": 1,
                "option": "Esta maravilhoso!",
                "votes": 11
            },
            {
                "id": 2,
                "option": "Pode melhorar.",
                "votes": 6
            },
            {
                "id": 3,
                "option": "Nem sei como cheguei aqui...",
                "votes": 2
            }
        ]
    }

```

```
 http --form PUT http://ldepaulaf.pythonanywhere.com/api/surveys/1 description="Novo titulo" active=False -a admin:globoadmin
```
```

{
    "active": false,
    "description": "Novo titulo",
    "id": 1,
    "options": [
            {
                "id": 1,
                "option": "Esta maravilhoso!",
                "votes": 11
            },
            {
                "id": 2,
                "option": "Pode melhorar.",
                "votes": 6
            },
            {
                "id": 3,
                "option": "Nem sei como cheguei aqui...",
                "votes": 2
            }
    ]
}


```

```
 http --form POST http://ldepaulaf.pythonanywhere.com/api/options/ option="Novo Option" survey=2 -a admin:globoadmin
```
```
{
    "id": 16,
    "option": "Novo Option",
    "survey": 2,
    "votes": 0
}
```
```
http --form PUT http://ldepaulaf.pythonanywhere.com/api/options/2/11 option='novo Option' -a admin:globoadmin
```
```
{
    "id": 11,
    "option": "novo Option",
    "survey": 2,
    "votes": 32
}
```
## Melhorias futuras

* criação de possibilidade de login por token

## Considerações finais

O trabalho levou em torno de 2 dias ( com 5 horas em sequencia) para ter sua base feita, melhorias e bonus foram feitos ao longo de commits diversos, aprendi (e ainda estou aprendendo) bastante com esse desafio, planejo continuar a mante-lo e expandir a ideia para projetos futuros.
