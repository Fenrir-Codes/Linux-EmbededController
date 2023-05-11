#! /bin/python

from sense_hat import SenseHat
import time
from datetime import datetime
import signal 
import sys

sense = SenseHat()

hour_color = (0, 255, 0)#green
minute_color = (0, 0, 255)#blue
second_color = (255, 0, 0) #red
am_color = (255,255,0) #gul
pm_color = (0,255,255) #cyan
off = (0, 0, 0) #off color
choice = "up" #choice default UP

sense.show_message("Programmet starter", 0.05)# message to show at start

sense.clear() #clear diodes

def display_binary(value, row, color):
    #setting color on a diode if there should show 6 columns
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
    #setting color on a diode if there should show 6 columns
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


#push up event
def pushed_up(event):
    #if the joy is pressed up and released, show time in 24 hours format in 3 rows
    if event.action == "pressed":
        sense.clear()  
        print("up")
        global choice
        choice = "up"

# push down event
def pushed_down(event):
    #if joy is pressed down and released, show time in 12 hours format i 3 rown
    if event.action == "pressed":
        sense.clear()  
        print("down")
        global choice
        choice = "down"
    elif event.direction == "down" and event.action == "held":
        print("Holding")
        choice = "held"

#push left event
def pushed_left(event):
    #if joy is pressed left and released, show time in 24 hour format in 6 columns
    if event.action == "pressed":
        sense.clear()  
        print("left")
        global choice
        choice = "left"

#push right event
def pushed_right(event):
    #if the joy pressed right, show time in 12 hour format in 6 columns
    if event.direction == "right" and event.action == "pressed":
        sense.clear()  
        print("right")
        global choice
        choice = "right" 

#middle event EXIT
def joy_pressed(event):
    #if the joy middle is pressed = exit
    if event.direction == "middle" and event.action == "pressed":
        sense.clear()
        print("Middle Pressed")
        global choice
        choice = "pressed"


print(choice) # print your choice to terminal
        
# sense joystick events calling definitions
sense.stick.direction_up = pushed_up # if pushed up
sense.stick.direction_down = pushed_down # if pushed down
sense.stick.direction_left = pushed_left #if pushed left
sense.stick.direction_right = pushed_right # if pushed right
sense.stick.direction_middle = joy_pressed # joy middle pressed event

while True:    
    # the loop showing time in the chosen format
    t = datetime.now() #current time and date
    # print(t)
    if choice == "up":  # 24 hour format in 3 rows
        display_binary(t.hour, 3, hour_color)
        display_binary(t.minute, 4, minute_color)
        display_binary(t.second, 5, second_color)
        time.sleep(0.01)
    elif choice == "down": #12 hours format in 3 rows
        display_binary(int(t.strftime("%I")), 3, hour_color) #Hour (12-hour clock) as a decimal number.
        display_binary(t.minute, 4, minute_color)
        display_binary(t.second, 5, second_color)
        display_binary(t.strftime("%p"), 0, None)  # Indicates if it is AM or PM,(Am/PM) = AM : yellow  PM :  cyan'ish
        #sense.show_message(t.strftime("%H:%M:%S %p"))
        time.sleep(0.01)
    elif choice == "left": #24 timers format i 6 colonner
        display_binary_col(t.hour, 0, hour_color)
        display_binary_col(t.minute, 3, minute_color)
        display_binary_col(t.second, 6, second_color)
        time.sleep(0.01)
    elif choice == "right":  #12 timers format i 6 colonner
        display_binary_col(int(t.strftime("%I")), 0, hour_color) #Hour (12-hour clock) as a decimal number.
        display_binary_col(t.minute, 3, minute_color)
        display_binary_col(t.second, 6, second_color)
        display_binary_col(t.strftime("%p"), 0, None) # Indicates if it is AM or PM,(Am/PM) = AM : yellow  PM :  cyan'ish
        time.sleep(0.01)
    elif choice == "held":
         #if holding joy DOWN -> holddown show with digits
            sense.show_message(t.strftime("%H:%M:%S %p"))
    elif choice == "pressed":
        #exit the program
        sense.show_message("Programmet slutter", 0.05)
        sys.exit(0)
