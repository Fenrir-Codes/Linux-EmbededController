from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

while True:
    hour = int(sense.get_humidity())
    minute = int(sense.get_pressure())
    second = int(sense.get_temperature())
    
    hour_bin = '{0:b}'.format(hour).zfill(8)
    minute_bin = '{0:b}'.format(minute).zfill(8)
    second_bin = '{0:b}'.format(second).zfill(8)
    
    sense.clear()
    for i in range(8):
        sense.set_pixel(1,i, int(hour_bin[i]) * 255, 0, 0)
        sense.set_pixel(3,i, int(minute_bin[i]) * 255, 255, 0)
        sense.set_pixel(5,i, int(second_bin[i]) * 255, 255, 255)
        
    sleep(1)
    
    
    #-------------------------- changes ------------------------------------------
    
from sense_emu import SenseHat
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
    hour_digits = get_binary_digits(hour, 6)
    minute_digits = get_binary_digits(minute, 6)
    second_digits = get_binary_digits(second, 6)
    for i in range(6):
        sense.set_pixel(1, i+1, hour_digits[i]*255, hour_digits[i]*255, hour_digits[i]*255)
        sense.set_pixel(3, i+1, minute_digits[i]*255, minute_digits[i]*255, minute_digits[i]*255)
        sense.set_pixel(5, i+1, second_digits[i]*255, second_digits[i]*255, second_digits[i]*255)

while True:
    hour, minute, second = get_time()
    display_time(hour, minute, second)
    sleep(1)
