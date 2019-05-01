#!/usr/bin/python
import os
import sys
import wallaby

def close_claw():
    wallaby.set_servo_position(0, 556)
    wallaby.msleep(3000)

def open_claw():
    wallaby.set_servo_position(0, 1600)
    wallaby.msleep(3000)

def main():
    left = 0
    right = 1
    
    wallaby.enable_servo(0)
    open_claw()

    if not wallaby.camera_open():
        print "camera couldn't open!"
        return

    while True:
        if not wallaby.camera_update():
            continue
        objects = wallaby.get_object_count(0)
        if objects == 0:
            continue
        best = max((wallaby.get_object_confidence(0,i),i) for i in range(objects))[1]
        if wallaby.get_object_confidence(0, best) < .30:
            continue

        #multiplier = abs(wallaby.get_camera_width()/2 - wallaby.get_object_center_x(0, best))
        #speed = abs((-3/5)*multiplier + 23)
        #if speed < 0:
        #    continue
        if wallaby.get_object_center_x(0, best) > 0.5*wallaby.get_camera_width() - 5:
            #wallaby.ao()
            wallaby.motor(left, 50)
            wallaby.motor(right, 20)
            #wallaby.motor(right, speed)
            #print "right %d" % speed
        elif wallaby.get_object_center_x(0, best) < 0.5*wallaby.get_camera_width() + 5:
            #wallaby.ao()
            wallaby.motor(right, 50)
            wallaby.motor(left, 20)
            #wallaby.motor(left, speed)
            #print "left %d" % speed
        elif wallaby.get_object_center_x(0, best) == 0.5*wallaby.get_camera_width():
            wallaby.ao()
            wallaby.motor(left, 50)
            wallaby.motor(right, 50)

        if wallaby.get_object_bbox_uly(0, best) > wallaby.get_camera_height() *.8:
            wallaby.ao()
            wallaby.cmpc(0)
            wallaby.cmpc(1)
            wallaby.motor(0, 45)
            wallaby.motor(1, 50)
            while wallaby.gmpc(0) < 1200:
                continue
            wallaby.ao()
            close_claw()
            break

    wallaby.ao()
    wallaby.msleep(1000)

    wallaby.motor(0, -45)
    wallaby.motor(1, -50)
    while wallaby.analog(0) > 800:
        continue
    wallaby.ao()
    wallaby.msleep(1000)

    wallaby.motor(0, -45)
    wallaby.motor(1, -50)
    while wallaby.analog(0) < 800:
        continue
    wallaby.ao()
    wallaby.cmpc(0)
    wallaby.motor(0, 50)
    wallaby.motor(1, -50)
    while wallaby.gmpc(0) < 1100:
        continue
    wallaby.ao()
    open_claw()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
