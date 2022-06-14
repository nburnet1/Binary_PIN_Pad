from machine import Pin
from time import sleep

def clear_LED():#clears bin LEDs
    pin_2_8.value(0) 
    pin_3_4.value(0)
    pin_4_2.value(0)
    pin_5_1.value(0) 

def light_LED(light,index):#checks index and light bool
    if(not light):
        return index + 1
    
    if(index == 2):
        pin_2_8.value(1)
    elif(index == 3):
        pin_3_4.value(1)
    elif(index == 4):
        pin_4_2.value(1)
    else:
        pin_5_1.value(1)
        
    return index + 1

def enter_pin():
    pin = ""
    index = 2 #incrementing based on gpio 
    while True:
        #clears PIN values
        if(pin_28_clear.value() == 0):
            pin = ""
            print("PIN CLEARED")
            clear_LED()
            index = 2
            sleep(.25)
        
        if(pin_13_0.value() == 0):# zero button pressed
            pin += "0"
            print(pin)
            index = light_LED(False,index)
            sleep(.25)
        if(pin_14_1.value() == 0):# one button pressed
            pin += "1"
            print(pin)
            index = light_LED(True,index)
            sleep(.25)
        
        if(len(pin) == 4): #length limit reached
            clear_LED()
            index = 2
            result = int(pin,2)
            if(result == passcode):
                print("Correct!")
                pin_board.value(1)
                sleep(2)
                pin_board.value(0)
                pin = ""
            else:
                print("Wrong!")
                pin = ""
                pin_20_alarm.value(1)
                
                sleep(1)
                pin_20_alarm.value(0)
        
    
#set passcode
passcode = 15

#bin for zero
pin_13_0 = Pin(13,Pin.IN, Pin.PULL_UP)
#bin for one
pin_14_1 = Pin(14,Pin.IN, Pin.PULL_UP)
#onboard LED
pin_board = Pin(25,Pin.OUT)
#alarm Pin
pin_20_alarm = Pin(20,Pin.OUT)
#clear button
pin_28_clear = Pin(28,Pin.IN, Pin.PULL_UP)

#bin representation LEDs
pin_2_8 = Pin(2,Pin.OUT)#2^3
pin_3_4 = Pin(3,Pin.OUT)#2^2
pin_4_2 = Pin(4,Pin.OUT)#2^1
pin_5_1 = Pin(5,Pin.OUT)#2^0

#sets default values to 0
pin_20_alarm.value(0)
pin_board.value(0)
pin_2_8.value(0) 
pin_3_4.value(0)
pin_4_2.value(0)
pin_5_1.value(0)

#loop func
enter_pin()
