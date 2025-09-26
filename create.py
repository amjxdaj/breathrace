from db import cursor

class CreateAccount:
    def __init__(self):
        self.name = None
        self.username = None
        self.password = None

    def dataentry(self):
        self.name = input("Enter Your Name: ")
        self.username = self.usernamecheck()
        self.password = self.passcheck()
        self.dbinsertauth()
        self.usernamesend()
        return self.username  

    def usernamecheck(self):
        while True:
            username = input("Enter Your Username: ")
            cursor.execute('SELECT username FROM auth')
            usernames = [u[0] for u in cursor.fetchall()]

            if username in usernames:
                print("Username not available, try another.")
            else:
                print("Username available")
                return username

    def passcheck(self):
        while True:
            password = input("Enter Your Password: ")
            if len(password) < 6:
                print("Password must be at least 6 characters long.")
            else:
                return password

    def dbinsertauth(self):
        try:
            cursor.execute(
                'INSERT INTO auth(username, name, password) VALUES(%s, %s, %s)',
                (self.username, self.name, self.password)
            )
            print("✅ Account created successfully!")
        except Exception as e:
            print("Error inserting into database:", e)

    def usernamesend(self):
        return self.username