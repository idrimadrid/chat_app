from flask import Flask, render_template, redirect, url_for,session,request
from flask_socketio import SocketIO, send
import psycopg2
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
connection = psycopg2.connect("host='localhost' dbname='chat_db' user='postgres' password='admin'")
mycursor = connection.cursor()
socketio = SocketIO(app)


def insert_client(user,password):
    """    insert client into database    """
    sql = "INSERT INTO clients(UserName,Password, CreateDate) VALUES ('%s', '%s', '%s' );" % (user, password, datetime.now())
    try:
        mycursor.execute(sql)
        connection.commit()
    except:
        connection.rollback()

def insert_message(user,message):
    sql = "INSERT INTO messages(UserName,Messages, CreateDate) VALUES ('%s', '%s', '%s' );" % (user, message, datetime.now())
    try:
        mycursor.execute(sql)
        connection.commit()
    except:
        connection.rollback()

def get_client(user):
    sql = "SELECT UserName, Password FROM clients c WHERE c.UserName='%s'" % (user)
    mycursor.execute(sql)
    return mycursor.fetchall()

def get_message():
    sql = "SELECT UserName, Messages FROM messages "
    mycursor.execute(sql)
    return mycursor.fetchall()

@app.route('/')
def index():
	return redirect(url_for('login'))


@app.route('/login',methods=["POST","GET"])
def login():
    if "user" in session:
        return redirect('/chat')
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        client=get_client(username)
        cl=client[0]
        if cl[1] == password or "user" in session:
            session['user'] = username
            return redirect('/chat')
    return render_template('login.html')


@app.route('/register',methods=["POST","GET"])
def register():
    if "user" in session:
        return redirect('/chat')
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        insert_client(username,password)
        return redirect('/login')
    return render_template('register.html')


@socketio.on('message')
def handleMessage(usr,msg): 
    
    insert_message(session["user"],msg)
    msg = str(session["user"]+" : "+msg)
    print(msg)
    send(msg, broadcast=True)


@app.route('/chat')
def chat():
    return render_template('index.html',user=session["user"],messages=get_message())

@app.route('/logout')
def logout():
    session.pop("user")
    return redirect('/login')

if __name__ == '__main__':
    socketio.run(app, debug=True)