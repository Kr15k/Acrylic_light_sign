from machine import Pin, Timer
from neopixel import myNeopixel
import time
"""
import _thread
"""

NUM_LEDS = 38
np = myNeopixel(NUM_LEDS, 16)

rp = Pin(18, Pin.OUT)
gp = Pin(19, Pin.OUT)
bp = Pin(20, Pin.OUT)


"""
button = Pin(13, Pin.IN, Pin.PULL_UP)
"""

red = 0                  #red
green = 0                #green
blue = 0                 #blue

ledStrip = 3
# 1 = rainbow wheel
# 2 = white still
# 3 = white train
np.brightness(255) # light strenght (0-255)

"""
def buttonInput():
    while True:
        if not button.value():
            changeLightSettings()
                
_thread.start_new_thread(buttonInput, ())
"""

def wheel(pos):
    global red, green, blue
    WheelPos = pos % 255
    if WheelPos < 85:
        red = (255-WheelPos*3)
        green = (WheelPos*3)
        blue=0
    elif WheelPos >= 85 and WheelPos < 170:
        WheelPos -= 85;
        red = 0
        green = (255 - WheelPos*3)
        blue = (WheelPos*3)
    else :
        WheelPos -= 170;
        red = (WheelPos*3)
        green = 0
        blue = (255-WheelPos*3)
        
def RGBLoop():
    for i in range(0, 255):
        for j in range(0, 38):
            wheel(i + j*255 // 38)
            np.set_pixel(j, red, green, blue)
        np.show()
        time.sleep_ms(1)
            
def whiteStrip():
    for i in range(0, 38):
        red = 255
        green = 255
        blue = 255
        np.set_pixel(i, red, green, blue)
        np.show()

def oneLight():
    global ledStrip
    for i in range(0, 38):
        red = 255
        green = 255
        blue = 255
        np.set_pixel(i, red, green, blue)
        time.sleep_ms(30)
        np.set_pixel(i-10, 0, 0, 0)
        np.show()
             
def runLight():
    if ledStrip == 1:
        for do in range(0, 1): #9
            RGBLoop()
    elif ledStrip == 2:
        for do in range(0, 5): #60
            oneLight()
    elif ledStrip == 3:
            whiteStrip()
            time.sleep(3) #60

def changeLightSetting():
    global ledStrip
    if ledStrip == 3:
        ledStrip = 1
    elif ledStrip != 3:
        ledStrip += 1
    print (ledStrip)

def allOneColor():
    time.sleep_ms(500)
    for i in range(0, 38):
        red = 255
        green = 0
        blue = 0
        np.set_pixel(i, red, green, blue)
        np.show()
    bp.value(0)
    rp.value(1)
    time.sleep_ms(500)
    for i in range(0, 38):
        red = 0
        green = 255
        blue = 0
        np.set_pixel(i, red, green, blue)
        np.show()
    rp.value(0)
    gp.value(1)
    time.sleep_ms(500)
    for i in range(0, 38):
        red = 0
        green = 0
        blue = 255
        np.set_pixel(i, red, green, blue)
        np.show()
    gp.value(0)
    bp.value(1)

def otherStripFlash():
    bp.value(0)
    time.sleep_ms(200)
    bp.value(1)
    gp.value(0)
    time.sleep_ms(200)
    gp.value(1)
    rp.value(0)
    time.sleep_ms(200)
    rp.value(1)
    
    
    
def tick(timer):
    otherStripFlash()


while True:
    RGBLoop()
    
    #allOneColor()
    
    """
    
bp.value(1)
    changeLightSetting()
    runLight()
    
rp.value(1)
gp.value(1)
bp.value(1)
RGBLoop()
"""