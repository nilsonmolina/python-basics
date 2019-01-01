# pylint: disable=C0111, E1101
# - [C0111] WARNING: missing module, class docstrings.
# - [E1101] ERROR: Instance of SQLAlchemy has no 'Column' member
from db import db


class StoreModel(db.Model):
    # -------- SQLALCHEMY SETUP
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # items = db.relationship('ItemModel') # not lazy
    items = db.relationship('ItemModel', lazy='dynamic')

    # -------- CLASS METHODS
    def __init__(self, name):
        self.name = name

    def json(self):
        # return {'name': self.name, 'items': [item.json() for item in self.items]} # not lazy
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
