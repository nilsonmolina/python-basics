# pylint: disable=C0111,C0103
# - [C0111] WARNING: missing module, function docstrings.
# - [C0103] WARNING: constant names not UPPER_CASE style.
from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, 'bob', 'password')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)



# # ----------------------------------
# # SAME CODE IF CLASSES WERE NOT USED
# # ----------------------------------
# users = [
#     {
#         'id': 1,
#         'username': 'bob',
#         'password': 'password'
#     }
# ]

# username_mapping = {
#     'bob': {
#         'id': 1,
#         'username': 'bob',
#         'password': 'password'
#     }
# }

# userid_mapping = {
#     1: {
#         'id': 1,
#         'username': 'bob',
#         'password': 'password'
#     }
# }
