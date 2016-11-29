#reference: https://docs.python.org/2/library/sqlite3.html

import sqlite3


conn = sqlite3.connect('todolist.db')

def Database():
    c = conn.cursor()

    # Create table
    c.execute("CREATE TABLE IF NOT EXISTS todolist(item TEXT)")

    # Insert a row of data
    c.execute("INSERT INTO todolist(item) VALUES('pay bills')")

    #   Save (commit) the changes
    conn.commit()

    conn.close()
    
if __name__ == "__main__":
    Database()