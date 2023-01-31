from cs1robots import *

#create_world()


def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()


def step_back():
    hubo.turn_left()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    hubo.turn_left()




def jump():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()
'''
load_world('worlds/hurdles1.wld')
hubo = Robot()

hubo.move()
jump()
hubo.move()
jump()
hubo.move()
jump()
hubo.move()
jump()
hubo.move()
hubo.pick_beeper()
'''
load_world('worlds/newspaper.wld')
hubo = Robot

hubo.set_trace("blue")
hubo.set_pause(0.3)

def climb_up_stairs(): #계단오르기
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.move()

def turn_around():
    hubo.turn_left()
    hubo.turn_left()

def climb_down_stair():
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()

hubo.move()
climb_up_stairs()
climb_up_stairs()
climb_up_stairs()
climb_up_stairs()
hubo.drop_beeper()

turn_around()
hubo.move()
climb_down_stair()
climb_down_stair()
climb_down_stair()
climb_down_stair()