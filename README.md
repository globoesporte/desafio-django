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

Para ver o site em deploy no python anywhere, acesse http://ldepaulaf.pythonanywhere.com/ (ainda em processo de deploy)

Para as requisições use o usuario admin e a senha é globoadmin.


## Endpoints
Os endpoints são como seguem. Lembrando que o {id} representa o id da enquete ou da opção da enquete, de acordo como o endereço representado. O único que não precisa de autenticação é o /vote

| Caminho       | Método | Parametros | Descrição
| :---          |  :---: |       :---:      | ---: |
| /api/surveys       | POST   |      description, active       | Cria uma enquete |
| /api/surveys       | GET    | N/A              | Recupera as informações de todas as enquetes |
| /api/surveys/{id}    | GET    | N/A              | Recupera as informações de uma única enquete|
| /api/surveys/{id}    | PUT    | description, active              | Atualiza informações de uma enquete|
| /api/surveys/{id}    | DELETE | N/A              | Deleta uma enquete|
| /api/vote/survey\={id}/option\={id}          | POST   | N/A              | Vota em uma única enquete|
| /api/vote/survey\={id}/old_option\={id}/new_option\={id}        | PUT   | N/A              | Muda seu voto em uma única enquete|
| /api/vote/survey\={id}/option\={id}          | DELETE   | N/A              | Deleta seu voto em uma única enquete|
| /api/options      | POST   |  option, survey              | Cria uma nova opção de enquete|
| /api/options/survey\={id}/option\={id}    | PUT    | option              | Atualiza uma opção de enquete|
| /api/options/survey\={id}/option\={id}    | DELETE | N/A              | Deleta uma opção de enquete|

## Autenticação
Esse projeto utiliza [Basic Access Authetication](https://en.wikipedia.org/wiki/Basic_access_authentication) para fazer a autenticação em todos os endpoints protegidos. Para interagir com esses endpoints, é necessário passar suas credencias no header da chamada. Para facilitar a sua vida, eu recomendo usar o [httpie](https://httpie.org/) (o melhor é feito em python).

## View Django template

O site possui um único template, que mostra todas as enquetes (com uma animação de porcentagem em circulo). Para acessa-lo, é necessário visitar a url /surveys (como em http://ldepaulaf.pythonanywhere.com/surveys/)

## Melhorias futuras

*criação de testes
*melhoria do template
*verificação e casos para o API e restrições
*cache de memoria para otimização das ações


## Considerações finais

Por enquanto está muito anacabado ainda, o first commit foi trabalho de 4 horas de programação, agora com o bruto já feito a lapidação e melhoras devem ser razoavelmente rapidas
