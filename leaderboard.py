from db import cursor
from prettytable import PrettyTable

def fetching():
    cursor.execute("SELECT * FROM breath_data ORDER BY duration DESC")
    rows = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ["Rank", "Username", "Duration (s)"]

    for i, row in enumerate(rows, start=1):
        table.add_row([i, row[0], row[1]])
    print(table)

