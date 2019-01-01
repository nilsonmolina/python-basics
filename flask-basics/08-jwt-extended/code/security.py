# pylint: disable=C0111,C0103
# - [C0111] WARNING: missing module, function docstrings.
# - [C0103] WARNING: constant names not UPPER_CASE style.
from werkzeug.security import safe_str_cmp
from resources.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
