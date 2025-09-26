import time
from db import cursor
from accountmanage import choice

def stopwatch():
    input("Press Enter to start the timer...")
    start = time.time()
    input("Press Enter to stop...")
    stop = time.time()
    duration = round(stop - start, 2)
    print("Your Max Breath = ", duration)
    return duration

def dbinsertbreath(username, duration):
    try:
        cursor.execute(
            '''INSERT INTO breath_data(username, duration) 
               VALUES(%s, %s) 
               ON DUPLICATE KEY UPDATE duration = GREATEST(duration, VALUES(duration))''',
            (username, duration)
        )
        print("Data added/updated successfully!")
    except Exception as e:
        print("Error inserting into database:", e)

def main():
    while True:
        c = int(input("\n1. Register\n2. Login\n3. Leaderboard\n4. Exit\nEnter your choice : "))

        if c == 1:
            from create import CreateAccount
            ca = CreateAccount()
            username = ca.dataentry()
            if username:
                choice(username)
                
        elif c == 2:
            from login import login
            username = login()
            if username:
                choice(username)

        elif c == 3:
            from leaderboard import fetching
            fetching()

        elif c == 4:
            print("Exiting...")
            break

        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()
