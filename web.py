from flask import Flask, session, url_for, redirect, request
from flask_mysqldb import MySQL
import hashlib


### FLASK APP ###
app = Flask(__name__)


### DATABASE CONFIG ### 
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = '8799'
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_DB"] = 'main'
app.config["MYSQL_CURSORCLASS"] = 'DictCursor' 

mysql = MySQL(app)

### ENCRYPTION CONFIG ###
salt = "@bh@y"

### MAIN APP ###

@app.route("/app/agent", methods=['POST'])
def add_user():
    userId = request.args.get('agent_id')
    password = request.args.get('password') + salt
    h = hashlib.md5(password.encode())
    hashedPass = h.hexdigest()
    try:
        cur = mysql.connection.cursor()
        cur.execute(f"INSERT INTO agent VALUES('{userId}','{hashedPass}')")
        mysql.connection.commit()
        return {'status':'account created','status_code':200}
    except:
        return {'status':'failure','status_code':401}

@app.route("/app/agent/auth", methods=['POST'])
def login():
    id = request.args.get('agent_id')
    password = request.args.get('password') + salt
    h = hashlib.md5(password.encode())
    password = h.hexdigest()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM agent")
    users = cur.fetchall()

    for entry in users:
        if entry['id'] == id:
            if entry['password'] == password:
                return {'status':'success','agent_id':id,'status_code':200}
            else:
                break
    return {'status':'failure','status_code':401}


@app.route("/app/sites/list/",methods=['GET'])
def todo_list():
    id = request.args.get('agent')
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM tasks WHERE id='{id}' ORDER BY due_date")
    temp = cur.fetchall()
    ans = []
    for item in temp:
        string = f"|| TITLE: {item['title']} || DESCRIPTION: {item['description']} || CATEGORY: {item['category']} || DUE DATE: {item['due_date']}"
        ans.append(string)
    return {'Tasks':ans}
    return {'status':'user authentication error','status_code':401}

@app.route("/app/sites/",methods=['POST'])
def add_item():
    
    id = request.args.get('agent')
    title = request.args.get('title')
    desc = request.args.get('description')
    cat = request.args.get('category')
    due_date = request.args.get('due_date')
    cur = mysql.connection.cursor()
    cur.execute(f"INSERT INTO tasks (id,title,description,category,due_date) VALUES('{id}','{title}','{desc}','{cat}','{due_date}')")
    mysql.connection.commit()
    return {'status':'success','status_code':200}
if __name__ == "__main__":
    app.run(debug=True)
    