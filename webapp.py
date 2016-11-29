# Kelvin Murphy
#reference: https://github.com/data-representation/example-sqlite

import sqlite3
import flask as fl

DATABASE = 'todolist.db'

app = fl.Flask(__name__)

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/ToDo", methods=["GET", "POST"])
def todo():
    ToDo = (fl.request.values["userinput"])
    return ToDo
    conn = sqlite3.connect('todolist.db')

    c = conn.cursor()

    c.execute("INSERT into todolist(item) values(%s)", [ToDo])
    conn.commit()
    
    return ToDo

@app.route("/store", methods=["GET", "POST"])
def store():
    conn = sqlite3.connect('todolist.db')

    c = conn.cursor()

    # Create table
    c.execute("SELECT item from todolist")
    return str(c.fetchall())


if __name__ == "__main__":
    app.run()