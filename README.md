# **API Restful com informações de carros**

### Ferramentas Utilizadas:

1. Flask
2. Flask-RESTFUL
3. SQLAlchemy
4. Marshmallow
5. Postgresql

# Como rodar a API

### Clonando o Repositorio

> git clone https://github.com/tomaz-f/ApiCarros.git

### Criando um virtualenv e Instalando as dependencias

1. Utilize o pip para baixar as dependencias no projeto

> virtualenv .venv

> pip install -r requirements.txt

### Rodando a api

> flask run app

A api vai rodar no http://localhost:5000/carros

### Fazendo as requisiçoes

Utilize o postman ou qualquer outro programa para testar a api.

### EXEMPLO DE .env

>

    POSTGRES_USER=admin
    POSTGRES_PASSWORD=admin
    POSTGRES_DB=flask_db
    PGADMIN_DEFAULT_EMAIL=admin@gmail.com
    PGADMIN_DEFAULT_PASSWORD=admin
    DB_URL=postgresql+psycopg2:///main?user=admin&password=adminf
    PGDATA=/data/postgres
