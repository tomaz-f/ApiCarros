# Path: tests/test_carros_resource.py

from flaskr.database.connection import db
from flaskr.models.carro_db_model import Carro

# test db connection
def test_db_connection():
    assert db.session.query('1').from_statement('SELECT 1').all() == [('1',)]
    


def test_get_all_carros(client):
    response = client.get('/carros')
    assert response.status_code == 200
    assert len(response.json) == 0

    carro = Carro(marca='Fiat', nome='Uno',
                  tipo='Hatch', ano=2010, cor='Vermelho')
    db.session.add(carro)
    db.session.commit()

    response = client.get('/carros')
    assert response.status_code == 200
    assert len(response.json) == 1


def test_get_carro(client):
    carro = Carro(marca='Fiat', nome='Uno',
                  tipo='Hatch', ano=2010, cor='Vermelho')
    db.session.add(carro)
    db.session.commit()

    response = client.get(f'/carros/{carro.id}')
    assert response.status_code == 200
    assert response.json['marca'] == 'Fiat'
    assert response.json['nome'] == 'Uno'
    assert response.json['tipo'] == 'Hatch'
    assert response.json['ano'] == 2010
    assert response.json['cor'] == 'Vermelho'


def test_get_carro_not_found(client):
    response = client.get('/carros/1')
    assert response.status_code == 404
    assert response.json['message'] == 'Carro não encontrado'


def test_post_carro(client):
    data = {
        'marca': 'Fiat',
        'nome': 'Uno',
        'tipo': 'Hatch',
        'ano': 2010,
        'cor': 'Vermelho'
    }

    response = client.post('/carros', json=data)
    assert response.status_code == 201
    assert response.json['status'] == 'sucesso'
    assert response.json['data']['marca'] == 'Fiat'
    assert response.json['data']['nome'] == 'Uno'
    assert response.json['data']['tipo'] == 'Hatch'
    assert response.json['data']['ano'] == 2010
    assert response.json['data']['cor'] == 'Vermelho'


def test_post_carro_invalid_json(client):
    data = {
        'marca': 'Fiat',
        'nome': 'Uno',
        'tipo': 'Hatch',
        'ano': 2010,
    }

    response = client.post('/carros', json=data)
    assert response.status_code == 400
    assert response.json['message'] == 'Nenhuma informação foi enviada'


def test_post_carro_invalid_json_keys(client):
    data = {
        'marca': 'Fiat',
        'nome': 'Uno',
        'tipo': 'Hatch',
        'ano': 2010,
    }

    response = client.post('/carros', json=data)
    assert response.status_code == 400
    assert response.json['message'] == 'Nenhuma informação foi enviada'


def test_put_carro(client):
    carro = Carro(marca='Fiat', nome='Uno',
                  tipo='Hatch', ano=2010, cor='Vermelho')
    db.session.add(carro)
    db.session.commit()

    data = {
        'marca': 'Fiat',
        'nome': 'Uno',
        'tipo': 'Hatch',
        'ano': 2010,
        'cor': 'Preto'
    }

    response = client.put(f'/carros/{carro.id}', json=data)
    assert response.status_code == 204

    carro = Carro.query.get(carro.id)
    assert carro.cor == 'Preto'


def test_put_carro_inexistent(client):
    data = {
        'marca': 'Fiat',
        'nome': 'Uno',
        'tipo': 'Hatch',
        'ano': 2010,
        'cor': 'Preto'
    }

    response = client.put('/carros/1', json=data)
    assert response.status_code == 404
    assert response.json['message'] == 'Carro não encontrado'


def test_put_carro_invalid_json(client):
    data = {
        'marca': 'Fiat',
        'nome': 'Uno',
        'tipo': 'Hatch',
        'ano': 2010,
    }

    response = client.put('/carros/1', json=data)
    assert response.status_code == 400
    assert response.json['message'] == 'Nenhuma informação foi enviada'


def test_put_carro_invalid_json_keys(client):
    data = {
        'marca': 'Fiat',
        'nome': 'Uno',
        'tipo': 'Hatch',
        'ano': 2010,
    }

    response = client.put('/carros/1', json=data)
    assert response.status_code == 400
    assert response.json['message'] == 'Nenhuma informação foi enviada'


def test_delete_carro(client):
    carro = Carro(marca='Fiat', nome='Uno',
                  tipo='Hatch', ano=2010, cor='Vermelho')
    db.session.add(carro)
    db.session.commit()

    response = client.delete(f'/carros/{carro.id}')
    assert response.status_code == 204


def test_delete_carro_inexistent(client):
    response = client.delete('/carros/1')
    assert response.status_code == 404
    assert response.json['message'] == 'Carro não encontrado'
