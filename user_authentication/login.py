import GLOBAL as G  # this holds globally defined variables


def login(email: str, password: str):
    count = 0
    for user in G.ALL_USERS:
        if user[G.JSON_EMAIL] == email and user[G.JSON_PASSWORD] == password:
            G.LOGGED_USER = user
            G.LOGGED_USER_INDEX = count
            return G.VALID
        count += 1
    return G.NOT_VALID


def ask_login():
    while True:
        email = input('Please enter your email: ')
        password = input('Please enter your password: ')

        if email.strip() != 0 and password.strip() != 0:
            var = login(email, password)

            if var == G.NOT_VALID:
                print('Email or Password are incorrect')
                return G.NOT_VALID
            else:
                return G.VALID
