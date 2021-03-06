from gpiozero import Button
from signal import pause
import arrow

def water_high():
    print("Water High!")
    utc = arrow.utcnow()
    utc_local = utc.to('local')
    print("UTC time  - Water lever changed HIGH - at: {}".format(utc))
    print("Local time - Water level changed HIGH - at: {}".format(utc_local))



def water_low():
    print("Water Low!")
    utc = arrow.utcnow()
    utc_local = utc.to('local')
    print("UTC time  - Water lever changed LOW - at: {}".format(utc))
    print("Local time - Water level changed LOW - at: {}".format(utc_local))


button = Button(2)
button.when_pressed = water_high
button.when_released = water_low
print('*** Water Level Sensor Started ***')

pause()
print('..Running..')


