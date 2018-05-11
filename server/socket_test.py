from gpiozero import Button
from signal import pause
import arrow
import json


from flask import Flask, render_template
from flask_socketio import SocketIO, emit

log_file = "waterLevelLog.json"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ourlittlesecret!'
socketio = SocketIO(app)


print('*** Water Level Sensor Started ***')




@socketio.on('connect')
def test_connect():
    print('connected server-side')
    #emit_update(0)
    #time.sleep(10)
    #print('1')
    #emit_update(1)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@app.route('/')
def index():
    return render_template('index.html')

#def emit_update(water_level):
#    socketio.emit('my update', {'water-level': water_level})


# A function to run when a HIGH event is triggered
def water_high():
    print("Water High!")
    utc = arrow.utcnow()
    utc_local = utc.to('local')
    water_log = {'id':'000001', 'level':True, 'utc_time': str(utc), 'local_time': str(utc_local)}

    print("UTC time  - Water lever changed HIGH - at: {}".format(utc))
    print("Local time - Water level changed HIGH - at: {}".format(utc_local))

    socketio.emit('my update', {'water-level': '3'})

    with open(log_file, 'a') as f:
        json.dump(water_log, f, ensure_ascii=False)

# A function to run when a LOW event is triggered
def water_low():
    print("Water Low!")
    utc = arrow.utcnow()
    utc_local = utc.to('local')
    water_log = {'id':'000001', 'level':False, 'utc_time': str(utc), 'local_time': str(utc_local)}


    print("UTC time  - Water lever changed LOW - at: {}".format(utc))
    print("Local time - Water level changed LOW - at: {}".format(utc_local))


    with open(log_file, 'a') as f:
        json.dump(water_log, f, ensure_ascii=False)


button = Button(2)
button.when_pressed = water_high
button.when_released = water_low



if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
