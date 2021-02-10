from gpiozero import DigitalInputDevice
from gpiozero import DigitalOutputDevice
from time import sleep

#setup pins

resb = DigitalOutputDevice(14)
rwb = DigitalInputDevice(15)

a0 = DigitalInputDevice(4)
a1 = DigitalInputDevice(17)
a2 = DigitalInputDevice(27)
a3 = DigitalInputDevice(22)
a4 = DigitalInputDevice(10)
a5 = DigitalInputDevice(9)
a6 = DigitalInputDevice(11)
a7 = DigitalInputDevice(0)
a8 = DigitalInputDevice(5)
a9 = DigitalInputDevice(6)
a10 = DigitalInputDevice(13)
a11 = DigitalInputDevice(19)
a12 = DigitalInputDevice(26)
a13 = DigitalInputDevice(21)
a14 = DigitalInputDevice(20)
a15 = DigitalInputDevice(16)
clock = DigitalOutputDevice(3)

clock_state = False;

def clock_tick():
    global clock_state

    clock_state = not clock_state
    if clock_state:
        clock.on()
    else:
        clock.off()
    sleep(1)

resb.off()
clock_tick()
clock_tick()
clock_tick()
clock_tick()
resb.on()


while True:
    out = ""

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

    clock_tick()

