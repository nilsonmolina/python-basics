# pylint: disable=C0111,C0103
# - [C0111] WARNING: missing module, class docstrings.
# - [C0103] WARNING: "id" doesn't conform to snake_case convention.
import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        return cls.find_by("username", username)

    @classmethod
    def find_by_id(cls, _id):
        return cls.find_by("id", _id)

    @classmethod
    def find_by(cls, param, value):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = f"SELECT * FROM users WHERE {param}=?"
        result = cursor.execute(query, (value,))
        row = result.fetchone()
        user = cls(*row) if row else None

        connection.close()
        return user

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {'message': 'A user with that username already exists.'}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()
        return {"message": "User created successfully."}, 201
