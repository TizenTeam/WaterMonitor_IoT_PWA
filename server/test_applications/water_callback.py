from gpiozero import Button
from signal import pause

def water_high():
    print("Water High!")

def water_low():
    print("Water Low!")

button = Button(2)

button.when_pressed = water_high
button.when_released = water_low
print('*** Water Level Sensor Started ***')
pause()
print('..Running..')


