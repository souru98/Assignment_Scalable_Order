from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import requests
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)


def get_book(book_id):
    response = requests.get(f'http://127.0.0.1:4000/book/availability/{book_id}')
    return response.json()


def get_user(user_id):
    response = requests.get(f'http://127.0.0.1:8081/users/{user_id}')
    return response.json()


class Order(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    date_issued = db.Column(db.DateTime, nullable=False)
    date_returned = db.Column(db.DateTime)

    def json(self):
        return {'order_id': self.order_id, 'book_id': self.book_id, 'user_id': self.user_id,
                'date_issued': self.date_issued,
                'date_returned': self.date_returned}


with app.app_context():
    db.create_all()


def decrease_book_count(book_id, quantity):
    data = {'quantity': quantity}
    response = requests.put(f'http://127.0.0.1:4000/book/decrease/{book_id}', json=data)
    return response.status_code == 200


def increase_book_count(book_id, quantity):
    data = {'quantity': quantity}
    response = requests.put(f'http://127.0.0.1:4000/book/increase/{book_id}', json=data)
    return response.status_code == 200


# Test api
@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'hey there! This is test api for order service! :)'}), 200)


@app.route('/orders', methods=['POST'])
def place_order():
    try:
        data = request.get_json()
        book = get_book(data['book_id'])
        user = get_user(data['user_id'])

        if data['quantity'] > 0 and book['Book']['is_available'] and user is not None:
            print("post db commit")
            order = Order(book_id=data['book_id'], user_id=data['user_id'], date_issued=db.func.current_timestamp())
            db.session.add(order)
            db.session.commit()
            print("post db commit")
            decrease_book_count(data['book_id'], data['quantity'])
            return make_response(jsonify({'message': 'Order placed successfully'}), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'oops! something went wrong'}), 500)


@app.route('/orders/<int:order_id>', methods=['PUT'])
def return_book(order_id):
    try:
        data = request.get_json()
        order = Order.query.filter_by(order_id=order_id).first()
        if order:
            order.date_returned = db.func.current_timestamp()
            db.session.commit()
            increase_book_count(order.book_id, data['quantity'])

            return make_response(jsonify({'message': 'Book returned successfully'}), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'oops! something went wrong'}), 500)


@app.route('/orders', methods=['GET'])
def fetch_orders():
    try:
        orders = Order.query.all()
        return make_response(jsonify([{'order_id': order.order_id, 'book_id': order.book_id, 'user_id': order.user_id}
                                      for order in orders]), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'oops! something went wrong'}), 500)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
