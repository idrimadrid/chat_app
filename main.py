from flask import Flask, render_template, redirect, url_for
from flask_socketio import SocketIO
import psycopg2
app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)
connection = psycopg2.connect("host='localhost' dbname='movie_db' user='postgres' password='admin'")
mycursor = connection.cursor()
def insert_client():
    """
    insert client into database
    """
    sql = "INSERT INTO movies(id,title, geners) VALUES ('%s', '%s', '%s' );" % (row[0], row[1], row[2])
    try:
        # Execute the SQL command
        mycursor.execute(sql)
        # Commit your changes in the database
        connection.commit()
    except:
        # Rollback in case there is any error
        connection.rollback()
@app.route('/')
def sessions():
	return render_template('login.html')
    #return redirect(url_for('login'))

@app.route('/login')
def login():
	#return redirect(url_for('/'))
	return render_template('login.html')

@app.route('/register')
def register():
	return render_template('register.html')



@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)