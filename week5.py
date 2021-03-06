from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO 
RPi.GPIO.setmode(RPi.GPIO.BCM)

led1 = LED(14)
led2 = LED(17)
led3 = LED(18)

win = Tk()
win.title("Week 5")

myFont = tkinter.font.Font(family = 'Arial', size = 12, weight = "bold")

def led1Toggle():
    if led1.is_lit:
        led1.off()
        ledButton1["text"] = "Turn on LED 1"
    else:
        led1.on()
        ledButton1["text"] = "Turn off LED 1"

def led2Toggle():
    if led2.is_lit:
        led2.off()
        ledButton2["text"] = "Turn on LED 2"
    else:
        led2.on()
        ledButton2["text"] = "Turn off LED 2"

def led3Toggle():
    if led3.is_lit:
        led3.off()
        ledButton3["text"] = "Turn on LED 3"
    else:
        led3.on()
        ledButton3["text"] = "Turn off LED 3"

def exit():
    RPi.GPIO.cleanup()
    win.destroy()


ledButton1 = Button(win, text = 'Turn on LED 1', font = myFont, command = led1Toggle, bg = 'yellow', height = 1, width = 25)
ledButton1.grid(row = 0, column = 1)

ledButton2 = Button(win, text = 'Turn on LED 2', font = myFont, command = led2Toggle, bg = 'green', height = 1, width = 25)
ledButton2.grid(row = 1, column = 1)

ledButton3 = Button(win, text = 'Turn on LED 3', font = myFont, command = led3Toggle, bg = 'blue', height = 1, width = 25)
ledButton3.grid(row = 2, column = 1)

exitBut = Button(win, text = 'Exit', font = myFont, command = exit, bg = 'red', height = 1, width = 10)
exitBut.grid(row = 3, column = 1)

win.protocol("WM_DELETE_WINDOW", exit)

win.mainloop()
