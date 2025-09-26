from db import conn, cursor

def authdata():
    cursor.execute('select * from auth')
    data=cursor.fetchall()
    usernames=[]
    for user in data:
        usernames.append(user[0])
    return usernames

def passfinder(username):
    cursor.execute("SELECT password FROM auth WHERE username=%s", (username,))
    passofuser = cursor.fetchone()
    return passofuser[0] if passofuser else None

def login():
    loggedin=False
    usernames = authdata()
    while True:
        username = input('Enter your username: ')
        if username not in usernames:
            print(f'{username} not found. Try again.')
            continue

        password = input('Enter your password: ')
        if password == passfinder(username):
            print("Successfully Logged In")
            loggedin=True
            return username
        else:
            print("Password incorrect. Try again.")