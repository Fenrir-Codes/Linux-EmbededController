#! /bin/python

""" BinaryClock script, bruger sense hat til at vise et binært ur"""

from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time
from datetime import datetime
import signal 
import sys

sense = SenseHat()

def signal_term_handler(signal, frame):
    """ Håndtere afslutning af program """
    sense.show_message("Programmet slutter", 0.05)
    sys.exit(0)
signal.signal(signal.SIGTERM, signal_term_handler)
signal.signal(signal.SIGINT, signal_term_handler)

hour_color = (0, 255, 0)#green
minute_color = (0, 0, 255)#blue
second_color = (255, 0, 0) #red
am_color = (255,255,0)
pm_color = (0,255,255)
off = (0, 0, 0)
choice = "up"

sense.show_message("Programmet starter", 0.05)

sense.clear()

def display_binary(value, row, color):
    """ Sætter farve på en diode, når der skal vises 3 rækker"""
    if value == "AM":
        sense.set_pixel(0, 7, am_color)
    elif value == "PM":
        sense.set_pixel(0, 7, pm_color)
    else:
        binary_str = "{0:8b}".format(value)
        for x in range(0, 8):
            if binary_str[x] == "1":
                sense.set_pixel(x, row, color)
            else:
                sense.set_pixel(x, row, off)

def display_binary_col(value, column, color):
    """ Sætter farve på en diode, når der skal vises 6 colonner"""
    numbers = []
    if value == "AM":
        sense.set_pixel(0, 7, am_color)
    elif value == "PM":
        sense.set_pixel(0, 7, pm_color)
    else:
        if len(str(value)) == 1:
            value = "0" + str(value)
        value = [int(val) for val in str(value)]
        binary_str = "{0:4b}".format(value[1])
        for y in range(0, 4):
            if binary_str[y] == "1":
                sense.set_pixel(column+1, y, color)
            else:
                sense.set_pixel(column+1, y, off)

        binary_str = "{0:4b}".format(value[0])
        for y in range(0, 4):
            if binary_str[y] == "1":
                sense.set_pixel(column, y, color)
            else:
                sense.set_pixel(column, y, off)

def pushed_up(event):
    """ Joystick event 'up', sætter 24 timers format, i 3 rækker"""
    if event.action != ACTION_RELEASED:
        sense.clear()  
        print("up")
        global choice
        choice = "up"

def pushed_down(event):
    """ Joystick event 'down', sætter 12 timers format, i 3 rækker"""
    if event.action != ACTION_RELEASED:
        sense.clear()  
        print("down")
        global choice
        choice = "down"

def pushed_left(event):
    """ Joystick event 'left', sætter 24 timers format, i 6 colonner"""
    if event.action != ACTION_RELEASED:
        sense.clear()  
        print("left")
        global choice
        choice = "left"

def pushed_right(event):
    """ Joystick event 'right', sætter 12 timers format, i 6 colonner"""
    if event.action != ACTION_RELEASED:
        sense.clear()  
        print("right")
        global choice
        choice = "right" 

def joy_pressed(event):
    """Hvis joystick trykket ned lukker programmet ned"""
    if event.action == ACTION_PRESSED:
        print("Middle Pressed")
        global choice
        choice = "pressed"
        

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = joy_pressed 

try:
    """ Prøver at bruge kommandolinje parameter, til at vælge hvilket ur der vises ved opstart"""
    i = sys.argv[1]
    u = sys.argv[2]

    if i == 'rows' and u == '24':
        choice = "up"
    elif i == 'rows' and u == '12':
        choice = "down"    
    elif i == 'columns' and u == '24':
        choice = "left"
    elif i == 'columns' and u == '12':
        choice = "right"
except:
    print("Except")

print(choice)

while True:    
    """ Loopet der holder scripet i gang, checker vad tiden er
    og fremviser tiden i det valgte format"""
    t = datetime.now()
    # print(t)
    if choice == "up":
        display_binary(t.hour, 3, hour_color)
        display_binary(t.minute, 4, minute_color)
        display_binary(t.second, 5, second_color)
        time.sleep(0.01)
    elif choice == "down":
        # print(t.strftime("%H:%M:%S %p"))
        display_binary(int(t.strftime("%I")), 3, hour_color)
        display_binary(t.minute, 4, minute_color)
        display_binary(t.second, 5, second_color)
        display_binary(t.strftime("%p"), 0, None)
        time.sleep(0.01)
    elif choice == "left":
        display_binary_col(t.hour, 0, hour_color)
        display_binary_col(t.minute, 3, minute_color)
        display_binary_col(t.second, 6, second_color)
        time.sleep(0.01)
    elif choice == "right":
        display_binary_col(int(t.strftime("%I")), 0, hour_color)
        display_binary_col(t.minute, 3, minute_color)
        display_binary_col(t.second, 6, second_color)
        display_binary_col(t.strftime("%p"), 0, None)
        time.sleep(0.01)
    elif choice == "pressed":
        """ Håndtere afslutning af program """
        sense.show_message("Programmet slutter", 0.05)
        sys.exit(0)
