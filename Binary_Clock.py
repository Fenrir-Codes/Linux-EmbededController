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