from cs1robots import *
'''
#Smart Hurdles----------------------------------

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

    else:
        jump()
'''


'''
#Smart ZigZag---------------------------------

create_world(10, 7)   
hubo = Robot()
hubo.set_trace('blue')
hubo.set_pause(0.1)

def turn_right():
    for i in range(3):
        hubo.turn_left()

for i in range(5):    #while을 어떻게 활용하지?
    hubo.turn_left()
    for j in range(6):
        hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    for j in range(6):
        hubo.move()
    if i != 4:
        hubo.turn_left()
        hubo.move()
'''

'''
#Return---------------------------------------------
#???몰라몰라
create_world()
hubo = Robot(orientation='W', avenue=7, street=5)
hubo.set_trace('blue')
hubo.set_pause(0.1)

while not hubo.front_is_clear() and not hubo.right_is_clear():
    if hubo.front_is_clear():
        hubo.move()
    elif not hubo.front_is_clear():
        hubo.turn_left()
        hubo.move()

hubo.facing_north()

'''

# #Trash1----------------------------------------------
#
# create_world()
# hubo = Robot(orientation='W', avenue=7, street=5)
# hubo.set_trace('blue')
# hubo.set_pause(0.1)


print(type(None))
