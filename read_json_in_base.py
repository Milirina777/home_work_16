import json
from base_connection import db
from bases import User, Offer, Order

# чтение данных из файлов
def read_json(file_name):
    with open(file_name, encoding='utf-8') as file:
        return json.load(file)

def users_to_dict(field):
    for row in field:
        db.session.add(
            User(
                id=row.get('id'),
                first_name=row.get('first_name'),
                last_name=row.get('last_name'),
                age=row.get('age'),
                email=row.get('email'),
                role=row.get('role'),
                phone=row.get('phone'),

            )
        )
        db.session.commit()


def orders_to_dict(field):
    for row in field:
        db.session.add(
            Order(
                id=row.get('id'),
                name=row.get('name'),
                description=row.get('description'),
                start_date=row.get('start_date'),
                end_date=row.get('end_date'),
                address=row.get('address'),
                price=row.get('price'),
                customer_id=row.get('customer_id'),
                executor_id=row.get('executor_id'),

            )
        )
        db.session.commit()


def offers_to_dict(field):
    for row in field:
        db.session.add(
            Offer(
                id=row.get('id'),
                order_id=row.get('order_id'),
                executor_id=row.get('executor_id'),

            )
        )
        db.session.commit()
