from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from bases import User, Order, Offer
from base_connection import db
from cut_config import Config
from read_json_in_base import read_json


app = Flask(__name__)

# создание вьюшек
@app.route("/users/", methods=["GET", "POST"])
def all_users():

    if request.method == "GET":
        users = db.session.query(User).all()
        base = []
        for item in users:
            base.append(item.data_output())
        return jsonify(base), 200

    elif request.method == "POST":
        data_json = read_json('./users.json')
        for item in data_json:
            user = User(**item)
            db.session.add(user)
        db.session.commit()

    return "User created", 201

@app.route("/users/<int:uid>", methods=["GET", "PUT", "DELETE"])
def some_user(uid):
    if request.method == "GET":
        return jsonify(db.session.query(User).filter(User.id == uid).first().data_output()), 200

    if request.method == "PUT":
        db.session.query(User).filter(User.id == uid).update(request.json)
        db.session.commit()

        return "User updated", 204

    if request.method == "DELETE":
        count = db.session.query(User).filter(User.id == uid).delete()
        db.session.commit()
        if not count:
            abort(404)

        return "User deleted", 204


@app.route("/orders", methods=["GET", "POST"])
def all_orders():
    if request.method == "GET":
        orders = db.session.query(Order).all()
        base = []
        for item in orders:
            base.append(item.data_output())
        return jsonify(base), 200

    elif request.method == "POST":
        data_json = read_json('./orders.json')
        for item in data_json:
            order = Order(**item)
            db.session.add(order)
        db.session.commit()

    return "Order created", 201


@app.route("/orders/<int:uid>", methods=["GET", "PUT", "DELETE"])
def some_order(uid):
    if request.method == "GET":
        return jsonify(db.session.query(Order).filter(Order.id == uid).first().data_output()), 200

    if request.method == "PUT":
        db.session.query(Order).filter(Order.id == uid).update(request.json)
        db.session.commit()

        return "Order updated", 204

    if request.method == "DELETE":
        count = db.session.query(Order).filter(Order.id == uid).delete()
        db.session.commit()
        if not count:
            abort(404)

        return "Order deleted", 204


@app.route("/offers", methods=["GET", "POST"])
def all_offers():

    if request.method == "GET":
        offers = db.session.query(Offer).all()
        base = []
        for item in offers:
            base.append(item.data_output())
        return jsonify(base), 200

    elif request.method == "POST":
        data_json = read_json('./offers.json')
        for item in data_json:
            offer = Offer(**item)
            db.session.add(offer)
        db.session.commit()

        return "Offer created", 201


@app.route("/offers/<int:uid>", methods=["GET", "PUT", "DELETE"])
def some_offer(uid):
    if request.method == "GET":
        return jsonify(db.session.query(Offer).filter(Offer.id == uid).first().data_output()), 200

    if request.method == "PUT":
        db.session.query(Offer).filter(Offer.id == uid).update(request.json)
        db.session.commit()

        return "Offer updated", 204

    if request.method == "DELETE":
        count = db.session.query(Offer).filter(Offer.id == uid).delete()
        db.session.commit()
        if not count:
            abort(404)

        return "Offer deleted", 204


if __name__ == "__main__":
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.drop_all()
        db.create_all()


    app.run(debug=True)
