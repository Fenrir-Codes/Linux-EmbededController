# this is just for testing purposes!!!!


from sense_hat import SenseHat
from time import sleep
import datetime

sense = SenseHat()

def get_time():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    return hour, minute, second

def get_binary_digits(value, num_bits):
    binary_digits = []
    for i in range(num_bits):
        binary_digits.append(value % 2)
        value //= 2
    return binary_digits

def display_time(hour, minute, second):
    hour_digits = get_binary_digits(hour % 12, 4)
    minute_digits = get_binary_digits(minute, 4)
    second_digits = get_binary_digits(second, 4)
    for i in range(4):
        sense.set_pixel(1, i+1, hour_digits[i]*255, hour_digits[i]*255, hour_digits[i]*255)
        sense.set_pixel(3, i+1, minute_digits[i]*255, minute_digits[i]*255, minute_digits[i]*255)
        sense.set_pixel(5, i+1, second_digits[i]*255, second_digits[i]*255, second_digits[i]*255)
    am_pm = 'AM' if hour < 12 else 'PM'
    hour = hour % 12
    if hour == 0:
        hour = 12
    time_str = '{:d}:{:02d}:{:02d} {}'.format(hour, minute, second, am_pm)
    for i, c in enumerate(time_str):
        sense.set_pixel(0+i, 6, 255, 255, 255 if c != ' ' else 0)
    sleep(1)

while True:
    hour, minute, second = get_time()
    display_time(hour, minute, second)
    
    
    
    #------------------------- changes ------------------------------------------------------------------
    
from sense_hat import SenseHat
from time import sleep
import datetime

sense = SenseHat()

def get_time():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    return hour, minute, second

def get_binary_digits(value, num_bits):
    binary_digits = []
    for i in range(num_bits):
        binary_digits.append(value % 2)
        value //= 2
    return binary_digits

def display_binary_clock(hour, minute, second):
    hour_digits = get_binary_digits(hour, 8)
    minute_digits = get_binary_digits(minute, 8)
    second_digits = get_binary_digits(second, 8)
    for i in range(8):
        sense.set_pixel(1, i, hour_digits[i]*255, 0, 0)
        sense.set_pixel(3, i, minute_digits[i]*255, 255, 0)
        sense.set_pixel(5, i, second_digits[i]*255, 255, 255)

def display_12_hour_clock(hour, minute, second):
    hour_digits = get_binary_digits(hour % 12, 2)
    minute_digits = get_binary_digits(minute, 2)
    second_digits = get_binary_digits(second, 2)
    for i in range(2):
        sense.set_pixel(1, i+3, hour_digits[i]*255, hour_digits[i]*255, hour_digits[i]*255)
        sense.set_pixel(3, i+3, minute_digits[i]*255, minute_digits[i]*255, minute_digits[i]*255)
        sense.set_pixel(5, i+3, second_digits[i]*255, second_digits[i]*255, second_digits[i]*255)
    am_pm = 'AM' if hour < 12 else 'PM'
    hour = hour % 12
    if hour == 0:
        hour = 12
    time_str = '{:d}:{:02d}:{:02d} {}'.format(hour, minute, second, am_pm)
    for i, c in enumerate(time_str):
        sense.set_pixel(0+i, 6, 255, 255, 255 if c != ' ' else 0)

display_mode = 'binary'

while True:
    hour, minute, second = get_time()
    if display_mode == 'binary':
        display_binary_clock(hour, minute, second)
    else:
        display_12_hour_clock(hour, minute, second)
    for event in sense.stick.get_events():
        if event.action == 'pressed' and event.direction == 'right':
            display_mode = '12_hour'
    sleep(0.1)

