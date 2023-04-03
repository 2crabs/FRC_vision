count = 0
cones = []
cubes = []
tag_id = 0
tag_x = 0
tag_y = 0
tag_dist = 0
active = 0

mode = 1

from machine import I2C
import time
import sensor
import image
import math

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA) # 160 x 120 pixel
sensor.run(1)
sensor.skip_frames(3)

def on_receive(data):
    global mode
    global count
    if data == 16:
        count = 0
        print("16")
    else:
        mode = data
    print("on_receive:",data)

def on_transmit():
    global tag_id
    global count
    print("on_transmit")
    count = count + 1
    return count

def on_event(event):
    print("on_event:",event)

i2c = I2C(I2C.I2C0, mode=I2C.MODE_SLAVE, scl=7, sda=8, addr = 1, addr_size=7, on_receive=on_receive, on_transmit=on_transmit, on_event=on_event)

while True:
    print(mode)
    if mode == 2:
        print("all good")
        img=sensor.snapshot()
        img.cartoon()
        tags = img.find_apriltags(roi = (0,0,320,160), families = image.TAG16H5)# defaults to TAG36H11 without “families”
        for tag in tags:
            img.draw_rectangle(tag.rect(), color = (255, 0, 0))
            img.draw_cross(tag.cx(), tag.cy(), color = (0, 255, 0))
            degress = 180 * tag.rotation() / math.pi
            print(tag.id(),tag.z_translation())
            tag_id = tag.id()



