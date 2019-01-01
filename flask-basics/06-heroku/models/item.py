# pylint: disable=C0111, E1101
# - [C0111] WARNING: missing module, class docstrings.
# - [E1101] ERROR: Instance of SQLAlchemy has no 'Column' member
from db import db


class ItemModel(db.Model):
    # -------- SQLALCHEMY SETUP
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    # -------- CLASS METHODS
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


# -------------- LEGACY CODE --------------
# # pylint: disable=C0111
# # - [C0111] WARNING: missing module, class docstrings.
# import sqlite3

# class ItemModel:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def json(self):
#         return {'name': self.name, 'price': self.price}

#     def insert(self):
#         connection = sqlite3.connect('data.db')
#         cursor = connection.cursor()

#         query = "INSERT INTO items VALUES (?, ?)"
#         cursor.execute(query, (self.name, self.price))

#         connection.commit()
#         connection.close()

#     def update(self):
#         connection = sqlite3.connect('data.db')
#         cursor = connection.cursor()

#         query = "UPDATE items SET price=? WHERE name=?"
#         cursor.execute(query, (self.price, self.name))

#         connection.commit()
#         connection.close()

#     @classmethod
#     def find_by_name(cls, name):
#         connection = sqlite3.connect('data.db')
#         cursor = connection.cursor()

#         query = "SELECT * FROM items WHERE name=?"
#         result = cursor.execute(query, (name,))
#         row = result.fetchone()
#         connection.close()

#         if row:
#             return cls(*row) # same as: cls(row[0], row[1])

#     @classmethod
#     def delete_by_name(cls, name):
#         connection = sqlite3.connect('data.db')
#         cursor = connection.cursor()

#         query = "DELETE FROM items WHERE name=?"
#         cursor.execute(query, (name,))

#         connection.commit()
#         connection.close()
