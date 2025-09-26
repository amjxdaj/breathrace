from db import cursor

def choice(username):
    while True:
        c = int(input("\n1. Record Max Breath\n2. Update Name\n3. Delete Account\n4. Back\nEnter your choice : "))

        if c == 1:
            from maxbreath import stopwatch, dbinsertbreath
            duration = stopwatch()
            dbinsertbreath(username, duration)

        elif c == 2:
            new_name = input("Enter Your New Name: ")
            try:
                cursor.execute("UPDATE auth SET name=%s WHERE username=%s", (new_name, username))
                print("Name updated successfully!")
            except Exception as e:
                print("Error updating name:", e)

        elif c == 3:
            try:
                cursor.execute("DELETE FROM auth WHERE username=%s", (username,))
                print("Account deleted successfully!")
                break
            except Exception as e:
                print("Error deleting account:", e)

        elif c == 4:
            break

        else:
            print("Invalid Choice, try again.")
