# Desafio Python/Django Globoesporte

Esse projeto é uma API em Python 3.6.3 usando Django 2.0.2 e Django Rest Framework 3.7.7 para poder criar, modificar e deletar enquetes. 

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

Para ver o site em deploy no python anywhere, acesse http://lucasavs.pythonanywhere.com/

O usuário (necessário para fazer as chamadas no endpoint que precisam de autenticação) se chama admin e a senha é adminadmin.


## Endpoints
Os endpoints são como seguem. Lembrando que o {id} representa o id da enquete ou da opção da enquete, de acordo como o endereço representado. O único que não precisa de autenticação é o /vote

| Caminho       | Método | Precisa de Corpo | Descrição
| :---          |  :---: |       :---:      | ---: |
| /survey       | POST   |         Sim      | Cria uma enquete |
| /survey       | GET    | Não              | Recupera as informações de todas as enquetes |
| /survey/{id}    | GET    | Não              | Recupera as informações de uma única enquete|
| /survey/{id}    | PUT    | Sim              | Atualiza informações de uma enquete|
| /survey/{id}    | DELETE | Não              | Deleta uma enquete|
| /vote         | POST   | Sim              | Vota em uma única enquete|
| /option      | POST   | Sim              | Cria uma nova opção de enquete|
| /option/{id}    | PUT    | Sim              | Atualiza uma opção de enquete|
| /option/{id}    | DELETE | Não              | Deleta uma opção de enquete|

## Autenticação
Esse projeto utiliza [Basic Access Authetication](https://en.wikipedia.org/wiki/Basic_access_authentication) para fazer a autenticação em todos os endpoints protegidos. Para interagir com esses endpoints, é necessário [criar um superuser](https://tutorial.djangogirls.org/pt/django_admin/) e passar suas credencias no header da chamada. Para facilitar a sua vida, eu recomendo usar o [Postman](https://www.getpostman.com/) para fazer as chamadas.

## Exemplos de corpo de chamadas 
Algumas chamadas nos endpoints precisam ter o seu body preenchido. Segue um exemplo de cada uma das chamadas que precisam desse campo preenchido. 

### POST /survey
```javascript
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
```

### PUT /survey/{id}
```javascript
{
    "name" : "Lista de comidas",
    "description": "Escolha a comida mais gostosa"
}
```

### POST /vote
```javascript
{
    "id": 999
}
```

### POST /option
```javascript
{
    "survey_id": 1,
    "description": "rabanada",
    "position": 6
}
```

### PUT /option/{id}
```javascript
{
    "description": "coxinha",
    "votes" : 50,
    "position": 10
}
```

## View Django template

O site possui um único template, que mostra todas as enquetes com o total de votos para cada opção. Para acessa-lo, é necessário visitar a url /surveys (como em http://lucasavs.pythonanywhere.com/surveys/)

## Melhorias futuras

* Pensar em alguma arquitetura com cache que permita salvar os votos a cada intervalo de tempo, sem que ela comprometa a resposta correta enquanto o voto ainda não foi escrito no banco de dado.
* Colocar mais informações relavantes na view de Admin.
* Melhorar o template de enquetes, permitindo inclusive votar por ela (Talvez usando React para fazer o trabalho)


## Considerações finais

Foi meu primeiro projeto usando Django e foi um processo de muito aprendizado. Estou aberto a críticas e sugestões a respeito da aplicação e espero que ela possa servir como base para outras pessoas que estejam dandos os primeiros passos com essa tecnologia.

Como sempre, estou sempre aberto a responder qualquer dúvida que possa surgir a qualquer momento.
