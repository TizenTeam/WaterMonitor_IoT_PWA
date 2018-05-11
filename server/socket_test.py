from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ourlittlesecret!'
socketio = SocketIO(app)

@socketio.on('connect')
def test_connect():
    print('connected server-side')
    emit_update(0)
    time.sleep(10)
    print('1')
    emit_update(1)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@app.route('/')
def index():
    return render_template('index.html')

def emit_update(water_level):
    socketio.emit('my update', {'water-level': water_level})

if __name__ == '__main__':
    socketio.run(app)
