from app.models.tables.situation_product import Situation_product
from app.models.tables.status_product import Status_product
from app.db_config import db


def create_seeds():
    situation_products = ['Longe a data', 'Proximo a data', 'Produto vencido']
    status_products = ['Ativo', 'Concluido']

    existing_situations = Situation_product.query.first()
    existing_statuses = Status_product.query.first()

    if existing_situations or existing_statuses:
        print("Seeds já foram criados.")
        return

    for name in situation_products:
        situation = Situation_product(name=name)
        db.session.add(situation)

    for name in status_products:
        status = Status_product(name=name)
        db.session.add(status)
    
    db.session.commit()
    db.session.close()
