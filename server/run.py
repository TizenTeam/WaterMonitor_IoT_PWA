from gpiozero import Button
from signal import pause
import arrow
import json

log_file = "waterLevelLog.json"




# A function to run when a HIGH event is triggered
def water_high():
    print("Water High!")
    utc = arrow.utcnow()
    utc_local = utc.to('local')
    water_log = {'id':'000001', 'level':True, 'utc_time': str(utc), 'local_time': str(utc_local)}

    print("UTC time  - Water lever changed HIGH - at: {}".format(utc))
    print("Local time - Water level changed HIGH - at: {}".format(utc_local))

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
print('*** Water Level Sensor Started ***')

pause()
print('..Running..')


