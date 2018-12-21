# pylint: disable=C0111,C0103
# - [C0111] WARNING: missing module, class docstrings.
# - [C0103] WARNING: "id" doesn't conform to snake_case convention.
class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
