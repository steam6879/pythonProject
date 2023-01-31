from cs1robots import *
'''
load_world('worlds/harvest3.wld')
hubo = Robot(beepers=100)
hubo.set_trace('blue')
hubo.set_pause(0.2)
'''
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def pick_and_move():
    if hubo.on_beeper():
        hubo.pick_beeper()
    hubo.move()

def plant_and_move():
    if not hubo.on_beeper():
        hubo.drop_beeper()
    hubo.move()

'''
 #Conditionals-Harvest
hubo.move()

for i  in range(3):  #[0, 1, 2]
    for j in range(5):
        pick_and_move()

    hubo.turn_left()
    pick_and_move()
    hubo.turn_left()

    for j in range(5):
        pick_and_move()

    if i != 2:
        turn_right()
        pick_and_move()
        turn_right()
'''

'''
#conditionals-Plant
hubo.move()

for i in range(3):  #[0, 1, 2]
    for j in range(5):
        plant_and_move()

    hubo.turn_left()
    plant_and_move()
    hubo.turn_left()

    for j in range(5):
        plant_and_move()

    if i != 2:
        turn_right()
        plant_and_move()
        turn_right()
'''
'''
load_world('worlds/harvest4.wld')
hubo = Robot(beepers=100)
hubo.set_trace('blue')
hubo.set_pause(0.2)

#While loop - Harvest Even More xx
hubo.move()

for i  in range(3):  #[0, 1, 2]
    for j in range(5):
        pick_and_move()

    hubo.turn_left()
    pick_and_move()
    hubo.turn_left()

    for j in range(5):
        pick_and_move()

    if i != 2:
        turn_right()
        pick_and_move()
        turn_right()
'''
'''
#Around the world
load_world('worlds/amazing2.wld')
hubo = Robot(beepers=100)
hubo.set_trace('blue')
hubo.set_pause(0.1)

hubo.drop_beeper()
hubo.move()
while not hubo.on_beeper():

    if hubo.right_is_clear():
        turn_right()
        hubo.move()
    elif hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()
hubo.pick_beeper()
'''


# load_world('worlds/amazing3.wld')
# hubo = Robot(beepers=100)
# hubo.set_trace('blue')
# hubo.set_pause(0.1)
#
# hubo.drop_beeper()
# hubo.turn_left()
# hubo.move()
# turn_right()
# hubo.move()
# while not hubo.on_beeper():
#
#     if hubo.right_is_clear():
#         turn_right()
#         hubo.move()
#     elif hubo.front_is_clear():
#         hubo.move()
#     else:
#         hubo.turn_left()
# hubo.pick_beeper()