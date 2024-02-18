# **Restful API using flask-restful**

## Clonando o Repositorio

> git clone <https://github.com/tomaz-f/ApiCarros.git>

## Criando um virtualenv e Instalando as dependencias

Utilize o virtualenv para criar um ambiente exclusivo para essa aplicação.

> python -m .venv venv

## Instales os pacotes necessarios

Utilize o aquivo de requirements juntamente com o pip para baixar as dependencias do projeto.

> pip install -r requirements.txt

## Rodando a api

> flask --app flaskr run --debug

A api vai rodar localmente: <http://localhost:5000/carros>

## Fazendo as requisiçoes

Utilize o postman ou qualquer outro programa para testar a api.

## EXEMPLO DE .env

>

    POSTGRES_USER=admin
    POSTGRES_PASSWORD=admin
    POSTGRES_DB=flask_db
    PGADMIN_DEFAULT_EMAIL=admin@gmail.com
    PGADMIN_DEFAULT_PASSWORD=admin
    DB_URL=postgresql+psycopg2://admin:admin@localhost:5432/flask_db
    PGDATA=/data/postgres
