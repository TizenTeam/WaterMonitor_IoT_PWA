from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ourlittlesecret!'
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app)
