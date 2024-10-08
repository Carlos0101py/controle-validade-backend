from app.models.tables.status_product import Status_product
from app.models.tables.category import Category
from app.db_config import db


def create_seeds():
    status_products = ['Ativo', 'Concluido']
    category_products = [
    'Frutas',
    'Vegetais',
    'Carnes',
    'Laticínios',
    'Pães e Produtos de Panificação',
    'Peixes e Frutos do Mar',
    'Ovos',
    'Salgadinhos',
    'Produtos Congelados',
    'Sucos e Bebidas',
    'Embutidos'
    ]
    
    existing_statuses = Status_product.query.first()
    existing_categors = Category.query.first()

    if existing_statuses and existing_categors:
        print("Seeds já foram criados.")
        return

    for name in status_products:
        status = Status_product(name=name)
        db.session.add(status)

    for name in category_products:
        category = Category(name=name)
        db.session.add(category)
    
    db.session.commit()
    db.session.close()
