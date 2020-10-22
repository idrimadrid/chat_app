from flask import Flask, render_template, redirect, url_for
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)
db = sql(app)

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