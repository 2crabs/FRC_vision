count = 0

from machine import I2C
import time

def on_receive(data):
    print("on_receive:",data)

def on_transmit():
    print("on_transmit, send:", count)
    return count

def on_event(event):
    print("on_event:",event)

i2c = I2C(I2C.I2C0, mode=I2C.MODE_SLAVE, scl=7, sda=8, addr = 1, addr_size=7, on_receive=on_receive, on_transmit=on_transmit, on_event=on_event)
while True:
    time.sleep_ms(500)
    count = count + 1;
    print(count)
