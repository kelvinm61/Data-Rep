# Kelvin Murphy
#reference: https://github.com/data-representation/example-sqlite
#import flask and sqlite3
import sqlite3
import flask as fl
#name databse
DATABASE = 'todolist.db'

app = fl.Flask(__name__)
#return answer in the html page index.
@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/ToDo", methods=["GET", "POST"])
def todo():
    ToDo = (fl.request.values["userinput"])
    return ToDo
    conn = sqlite3.connect('todolist.db')

    c = conn.cursor()
#sql commands in python that manipulates the database.
    c.execute("INSERT into todolist(item) values(%s)", [ToDo])
    conn.commit()
    
    return ToDo
#assigns info and requests for the html page.
@app.route("/store", methods=["GET", "POST"])
def store():
    conn = sqlite3.connect('todolist.db')

    c = conn.cursor()

    # Create table
    c.execute("SELECT * from todolist")
    return str(c.fetchall())


if __name__ == "__main__":
    app.run()