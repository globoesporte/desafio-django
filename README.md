# Desafio Python/Django Globoesporte

Desenvolva uma aplicação para criar, editar e deletar enquetes.

Crie um fork desse projeto e, quando concluído, faça um pull request do mesmo para esse repositório.

Vamos avaliar a organização do seu código e automações, então vale tomar cuidado.

Não existe um tempo determinado pra executar o teste, mas ele conta e é levado em consideração _Tempo x bônus executados x qualidade do código_.

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

## Bônus

No save dos votos, podemos ter uma carga muito grande. Para solucionar este problema, crie uma fila de votos na memória e a descarregue no banco a cada 1 minuto.

View Django template para a enquete (não precisa ficar bonito, mas não pode ser terrivelmente feio)

View Admin com dados interesantes sobre a enquete 

Testes unitários também são bem-vindos

Rodando em ambiente docker e deploy em Heroku ou PythonAnywhere


