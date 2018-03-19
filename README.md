# Desafio Python/Django Globoesporte

Desenvolva uma aplicação para criar, editar e deletar enquetes.

Crie um fork desse projeto, e quando concluído, crie um pull request do seu fork para esse repositório.

Vamos avaliar a organização do seu código e automações então vale tomar esse cuidado

Não existe um tempo determinado pra executar o teste mas ele conta e é levado em concideração Tempo x bonus executados x qualidade do código.

---

## Importante

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


## Instruções
Itens prontos:
    - As Apis para e páginas para serem criação de enquetes e suas páginas
    - A segurança só foi colocada nas rotas das views
    - A api foi escrita com DRF e Angular 1

Bônus prontos:
    - Para salvar as fotos a cada minuto, foi criada a classe VotoWorker no arquivo worker.py

Itens não entregues
    - Listagem para votação, só se pode votar através da listagem de enquetes
    - Não foram desenvolvidos testes unitários
    - A criação de uma imagem de container do docker não feita. Foi feita uma tentativa de deploy no Heroku, sem container através de push do GitHub e Heroku CLI, mas há algum erro na montagem da estrutura do projeto.

Instruções de uso
    - À partir da url "enquete/all" pode-se criar, alterar, excluir uma enquete, seus itens e efetuar uma votação.

