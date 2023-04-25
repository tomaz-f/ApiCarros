from app.models.carro_db_model import Carro
from app.schema.carros_schemas import CarroSchema, carros_schema, carro_schema
from app.database.connection import db


def test_carro_schema():
    carro = Carro(marca='Fiat', nome='Uno',
                  tipo='Hatch', ano=2010, cor='Vermelho')
    db.session.add(carro)
    db.session.commit()

    result = CarroSchema.dump(carro)
    assert result['marca'] == 'Fiat'
    assert result['nome'] == 'Uno'
    assert result['tipo'] == 'Hatch'
    assert result['ano'] == 2010
    assert result['cor'] == 'Vermelho'


def test_carros_schema():
    carro = Carro(marca='Fiat', nome='Uno',
                  tipo='Hatch', ano=2010, cor='Vermelho')
    db.session.add(carro)
    db.session.commit()

    result = carros_schema.dump(Carro.query.all())
    assert len(result) == 1
    assert result[0]['marca'] == 'Fiat'
    assert result[0]['nome'] == 'Uno'
    assert result[0]['tipo'] == 'Hatch'
    assert result[0]['ano'] == 2010
    assert result[0]['cor'] == 'Vermelho'


def test_carro_schema_update():
    carro = Carro(marca='Fiat', nome='Uno',
                  tipo='Hatch', ano=2010, cor='Vermelho')
    db.session.add(carro)
    db.session.commit()

    result = carro_schema.dump(carro)
    assert result['marca'] == 'Fiat'
    assert result['nome'] == 'Uno'
    assert result['tipo'] == 'Hatch'
    assert result['ano'] == 2010
    assert result['cor'] == 'Vermelho'

    carro.marca = 'Fiat'
    carro.nome = 'Uno'
    carro.tipo = 'Hatch'
    carro.ano = 2010
    carro.cor = 'Preto'

    result = carro_schema.dump(carro)
    assert result['marca'] == 'Fiat'
    assert result['nome'] == 'Uno'
    assert result['tipo'] == 'Hatch'
    assert result['ano'] == 2010
    assert result['cor'] == 'Preto'


def test_carro_schema_delete():
    carro = Carro(marca='Fiat', nome='Uno',
                  tipo='Hatch', ano=2010, cor='Vermelho')
    db.session.add(carro)
    db.session.commit()

    result = carro_schema.dump(carro)
    assert result['marca'] == 'Fiat'
    assert result['nome'] == 'Uno'
    assert result['tipo'] == 'Hatch'
    assert result['ano'] == 2010
    assert result['cor'] == 'Vermelho'

    db.session.delete(carro)
    db.session.commit()

    result = carro_schema.dump(carro)
    assert result == {}
