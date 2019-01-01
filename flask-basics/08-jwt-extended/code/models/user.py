# pylint: disable=C0111,E1101
# - [C0111] WARNING: missing module, class docstrings.
# - [E1101] ERROR: Instance of SQLAlchemy has no 'Column' member
from db import db


class UserModel(db.Model):
    # -------- SQLALCHEMY SETUP
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    # -------- CLASS METHODS
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


# -------------- LEGACY CODE --------------
# # pylint: disable=C0111,C0103
# # - [C0111] WARNING: missing module, class docstrings.
# # - [C0103] WARNING: "id" doesn't conform to snake_case convention.
# import sqlite3

# class UserModel:
#     def __init__(self, _id, username, password):
#         self.id = _id
#         self.username = username
#         self.password = password

#     @classmethod
#     def find_by_username(cls, username):
#         return cls.find_by("username", username)

#     @classmethod
#     def find_by_id(cls, _id):
#         return cls.find_by("id", _id)

#     @classmethod
#     def find_by(cls, param, value):
#         connection = sqlite3.connect('data.db')
#         cursor = connection.cursor()

#         query = f"SELECT * FROM users WHERE {param}=?"
#         result = cursor.execute(query, (value,))
#         row = result.fetchone()
#         user = cls(*row) if row else None

#         connection.close()
#         return user
