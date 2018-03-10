# Desafio Python/Django Globoesporte

Aplicação para criar, editar e deletar enquetes.

---

## Requerimentos

- Python 3.6
- Django 1.11
- Django REST Framework 3.7.7

---

## Instalação:

* Recomenda-se utilizar o virtualenvwrapper para trabalhar melhor com as versões utilizadas no projeto e evitar conflitos em outros projetos:

    $ pip install virtualenvwrapper

    $ /usr/local/bin/virtualenvwrapper.sh 

    $ echo "export WORKON_HOME=~/.virtualenvs" >> ~/.bash_profile

    $ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bash_profile 

    $ source ~/.bash_profile  


* Após fazer a instalação, podemos seguir com o setup do ambiente e a instalação dos pacotes necessários:

    $ mkvirtualenv enquete-ge

    $ workon enquete-ge

    $ make install
   
---

## Utilizando o Makefile:

- Os comandos a seguir devem ser utilizados na raíz do projeto

#####  Iniciando a Aplicação:
 
    $ make run

#####  Aplicando migrações:
 
    $ make migrations

##### Iniciando Testes da Aplicação:
 
    $ make test

##### Criando um novo superusuario:
 
    $ make user

---

## Acessando Django API REST:

##### Documentação detalhada:
* /api/docs/

##### Urls base:
* /api/polls/
* /api/options/
* /api/vote/

---



