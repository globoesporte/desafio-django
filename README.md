Rodando o arquivo em Docker:
É muito simples. Primeiramente instale o composer para facilitar ao processo.https://docs.docker.com/compose/install/#install-compose 

com o composer instalado, basta ir na pasta do projeto e usar os seguintes comandos
docker-compose run web manage.py migrate
docker-compose build
docker-compose up

E imediatamente o docker estará funcionando na porta 8000 do localhost











# Desafio Python/Django Globoesporte

Desenvolva uma aplicação para criar, editar e deletar enquetes.

Crie um fork desse projeto, e quando concluído, crie um pull request do seu fork para esse repositório.

Vamos avaliar a organização do seu código e automações então vale tomar esse cuidado

Não existe um tempo determinado pra executar o teste mas ele conta e é levado em concideração Tempo x bonus executados x qualidade do código.

---

## Importamte

- Seguir a convenção PEP8
- Python 3.6
- Django 1.11 ou superior
- README com as instruções para rodar o projeto
- Entregar [API REST](http://www.django-rest-framework.org/) com EndPoints POST, GET, PUT e DELETE
- O EndPoint para salvar o voto é o unico que não é autenticado
- Admin com campo para busca e filtros
- Arquivo requirements.txt na raiz do projeto com todas as dependências

---

## Bonus

No save dos votos, podemos ter uma carga muito grande de votos. Para solucionar este problema, crie uma fila de votos na memória e descarregue no banco a cada 1 minuto.

View Django template para a enquete (não precisa ficar bonito, mas não pode ser terrivelmente feio)

View Admin com dados interesantes sobre a enquete 

Testes unitários também são bem-vindos

Rodando em ambiente docker e deploy em Heroku ou PythonAnywhere


