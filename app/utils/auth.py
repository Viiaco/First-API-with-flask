from app import auth

USERS = {
    "admin": "secret",
    "user": "password",
    "test" : "1234"
}

@auth.verify_password
def verify_password(username, password):
    if username in USERS and USERS[username] == password:
        return username
    return None