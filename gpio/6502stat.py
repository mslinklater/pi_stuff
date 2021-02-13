from gpiozero import DigitalInputDevice
from gpiozero import DigitalOutputDevice
from time import sleep

#setup pins

resb = DigitalOutputDevice(3)
rwb = DigitalInputDevice(14)
clock = DigitalOutputDevice(4)

d0 = DigitalOutputDevice(15)
d1 = DigitalOutputDevice(18)
d2 = DigitalOutputDevice(23)
d3 = DigitalOutputDevice(24)
d4 = DigitalOutputDevice(25)
d5 = DigitalOutputDevice(8)
d6 = DigitalOutputDevice(7)
d7 = DigitalOutputDevice(1)

a0 = DigitalInputDevice(17)
a1 = DigitalInputDevice(27)
a2 = DigitalInputDevice(22)
a3 = DigitalInputDevice(10)
a4 = DigitalInputDevice(9)
a5 = DigitalInputDevice(11)
a6 = DigitalInputDevice(0)
a7 = DigitalInputDevice(5)
a8 = DigitalInputDevice(6)
a9 = DigitalInputDevice(13)
a10 = DigitalInputDevice(19)
a11 = DigitalInputDevice(26)
a12 = DigitalInputDevice(21)
a13 = DigitalInputDevice(20)
a14 = DigitalInputDevice(16)
a15 = DigitalInputDevice(12)

clock_state = False;

def clock_tick():
    global clock_state

    clock_state = not clock_state
    if clock_state:
        clock.on()
    else:
        clock.off()

    if True:
        out = ""

        if not resb.is_active:
            out += "RESET"

        if clock_state:
            out += "+ "
        else:
            out += "- "
            
        if rwb.is_active:
            out += "RWB+ "
        else:
            out += "RWB- "

        # address bus

        if a15.is_active:
            out += "1"
        else:
            out += "0"

        if a14.is_active:
            out += "1"
        else:
            out += "0"

        if a13.is_active:
            out += "1"
        else:
            out += "0"

        if a12.is_active:
            out += "1"
        else:
            out += "0"

        if a11.is_active:
            out += "1"
        else:
            out += "0"

        if a10.is_active:
            out += "1"
        else:
            out += "0"

        if a9.is_active:
            out += "1"
        else:
            out += "0"

        if a8.is_active:
            out += "1"
        else:
            out += "0"

        if a7.is_active:
            out += "1"
        else:
            out += "0"

        if a6.is_active:
            out += "1"
        else:
            out += "0"

        if a5.is_active:
            out += "1"
        else:
            out += "0"

        if a4.is_active:
            out += "1"
        else:
            out += "0"

        if a3.is_active:
            out += "1"
        else:
            out += "0"

        if a2.is_active:
            out += "1"
        else:
            out += "0"

        if a1.is_active:
            out += "1"
        else:
            out += "0"

        if a0.is_active:
            out += "1"
        else:
            out += "0"

        print(out)        
    
    sleep(.1)

#0xEA
d0.off()
d1.on()
d2.off()
d3.on()
d4.off()
d5.on()
d6.on()
d7.on()

resb.off()
clock_tick()
clock_tick()
clock_tick()
clock_tick()
clock_tick()
clock_tick()
clock_tick()
clock_tick()
clock_tick()
clock_tick()
resb.on()


while True:

    clock_tick()

