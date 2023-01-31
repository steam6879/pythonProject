#12221521 임정빈
from cs1robots import *

'''
#Task1. Smart Hurdles----------------------------------

load_world('worlds/hurdles3.wld')   
hubo = Robot()
hubo.set_trace('blue')
hubo.set_pause(0.1)

def turn_right():
    for i in range(3):
        hubo.turn_left()

def jump():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()

while not hubo.on_beeper():
    if hubo.front_is_clear():
        hubo.move()

    else:                        #허들을 마주쳤을때 점프
        jump()
'''

'''
#Task2. Rain-----------------------------------------------------

load_world('worlds/rain1.wld')
hubo = Robot(orientation='E', avenue=2, street=6, beepers=100)
hubo.set_trace('blue')
hubo.set_pause(0.2)

def turn_right():
    for i in range(3):
        hubo.turn_left()

hubo.move()
hubo.drop_beeper()             #while문을 활용하기 위한 beeper
turn_right()
hubo.move()

while not hubo.on_beeper():

    if hubo.right_is_clear():  #beeper로 창문을 닫기
        hubo.drop_beeper()
        hubo.move()

    elif hubo.front_is_clear():  
        hubo.move()

    else:                     #모서리에서는 회전
        hubo.turn_left()

hubo.pick_beeper()            #세레모니(?)
turn_right()
'''