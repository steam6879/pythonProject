from cs1robots import *

# create_world()
# hubo = Robot()
# hubo.set_trace('purple')
# hubo.set_pause(0.1)
#
# #Task 1 : ZigZag
#
# def turn_right():
#     for i in range(3):
#         hubo.turn_left()
#
# hubo.turn_left()
#
# for j in range(5):
#     for k in range(9):
#         hubo.move()
#     turn_right()
#     hubo.move()
#     turn_right()
#     for k in range(9):
#         hubo.move()
#
#     if j != 4:
#         hubo.turn_left()
#         hubo.move()
#         hubo.turn_left()



# #Task 3 : Newspaper delivery
#
# load_world('worlds/newspaper.wld')
# hubo = Robot(beepers=1)
# hubo.set_trace('purple')
# hubo.set_pause(0.1)
#
# def turn_right():
#     for i in range(3):
#         hubo.turn_left()
#
# def up_stairs():
#     hubo.turn_left()
#     hubo.move()
#     turn_right()
#     hubo.move()
#
# def down_stairs():
#     hubo.move()
#     hubo.turn_left()
#     hubo.move()
#     turn_right()
#
# for i in range(4):
#     hubo.move()
#     up_stairs()
#
# hubo.move()
# hubo.drop_beeper()
#
# hubo.turn_left()
# hubo.turn_left()
#
# for j in range(4):
#     hubo.move()
#     down_stairs()
# hubo.move()



# #Task 4 : Harvest
#
# load_world('worlds/harvest1.wld')
# hubo = Robot()
# hubo.set_trace('purple')
# hubo.set_pause(0.1)
#
# def turn_right():
#     for i in range(3):
#         hubo.turn_left()
#
# def pick_and_move():
#     hubo.pick_beeper()
#     hubo.move()
#
# hubo.move()
#
# for i in range(3):
#
#     for j in range(5):
#         pick_and_move()
#
#     hubo.pick_beeper()
#     hubo.turn_left()
#     hubo.move()
#     hubo.turn_left()
#
#     for j in range(5):
#         pick_and_move()
#
#     if i != 2:
#         hubo.pick_beeper()
#         turn_right()
#         hubo.move()
#         turn_right()
# hubo.pick_beeper()



#Task 5 : Harvest again

load_world('worlds/harvest2.wld')
hubo = Robot()
hubo.set_trace('purple')
hubo.set_pause(0.1)

def turn_right():
    for i in range(3):
        hubo.turn_left()

def up():
    hubo.pick_beeper()
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()

def down():
    hubo.pick_beeper()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()

for j in range(5):
    hubo.move()
hubo.turn_left()
hubo.move()
turn_right()

for k in range(3):
    for l in range(5):
        up()
    hubo.pick_beeper()

    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    hubo.move()

    for m in range(5):
        down()
    hubo.pick_beeper()

    if k!=2:
        hubo.move()
        turn_right()
        hubo.move()
        turn_right()



# #Task 1 : Conditionals - Harvest more
#
# load_world('worlds/harvest3.wld')
# hubo = Robot(beepers=100)
# hubo.set_trace('purple')
# hubo.set_pause(0.1)
#
# def turn_right():
#     for i in range(3):
#         hubo.turn_left()
#
# def pick_and_move():
#     if hubo.on_beeper():
#         hubo.pick_beeper()
#         hubo.move()
#
#     else:
#         hubo.move()
#
# hubo.move()
#
# for j in range(3):
#     for i in range(5):
#         pick_and_move()
#
#     hubo.turn_left()
#     pick_and_move()
#     hubo.turn_left()
#     for i in range(5):
#         pick_and_move()
#
#     if j != 2:
#         turn_right()
#         pick_and_move()
#         turn_right()



# #Task 2 : Conditionals-Plant
#
# load_world('worlds/harvest3.wld')
# hubo = Robot(beepers=100)
# hubo.set_trace('purple')
# hubo.set_pause(0.1)
#
# def turn_right():
#     for i in range(3):
#         hubo.turn_left()
#
# def drop_and_move():
#     if not hubo.on_beeper():
#         hubo.drop_beeper()
#         hubo.move()
#
#     else:
#         hubo.move()
#
# hubo.move()
#
# for j in range(3):
#     for i in range(5):
#         drop_and_move()
#
#     hubo.turn_left()
#     drop_and_move()
#     hubo.turn_left()
#     for i in range(5):
#         drop_and_move()
#
#     if j != 2:
#         turn_right()
#         drop_and_move()
#         turn_right()
#
#     else:
#         hubo.drop_beeper()


#
# #While loop - Smart ZigZag
#
# create_world(10,5)
# hubo = Robot(beepers=100)
# hubo.set_trace('purple')
# hubo.set_pause(0.1)
#
# def turn_right():
#     for i in range(3):
#         hubo.turn_left()
#
# def move_to_wall():
#     while hubo.front_is_clear():
#         hubo.move()
#
# def round_trip():
#     move_to_wall()
#
#     if hubo.front_is_clear():
#         hubo.move()
#         turn_right()
#         move_to_wall()
#         hubo.turn_left()
#
#         if hubo.front_is_clear():
#             hubo.move()
#             hubo.turn_left()
#
# hubo.turn_left()
#
# while hubo.front_is_clear():
#     round_trip()



# #Return
#
# create_world()
# hubo = Robot(orientation="W", avenue=8, street=6)
# hubo.set_trace('purple')
# hubo.set_pause(0.1)
#
# def turn_right():
#     for i in range(3):
#         hubo.turn_left()
#
# def move_to_wall():
#     while hubo.front_is_clear():
#         hubo.move()
#
# while not hubo.facing_north():
#     hubo.turn_left()
#
# for i in range(2):
#
#     hubo.turn_left()
#     move_to_wall()



# #Trash1
#
# load_world('worlds/trash2.wld')
# hubo = Robot()
# hubo.set_trace('purple')
# hubo.set_pause(0.1)
#
# def turn_right():
#     for i in range(3):
#         hubo.turn_left()
#
# def move_to_wall():
#     while hubo.front_is_clear():
#         hubo.move()
#
#         while hubo.on_beeper():
#             hubo.pick_beeper()
#
# if not hubo.on_beeper():
#     move_to_wall()
#
# hubo.turn_left()
# hubo.turn_left()
#
# move_to_wall()
#
# turn_right()
# hubo.move()
#
# while hubo.carries_beepers():
#     hubo.drop_beeper()
#
# hubo.turn_left()
# hubo.turn_left()
#
# hubo.move()


# trash
#
# load_world('worlds/trash2.wld')
# hubo=Robot()
# hubo.set_pause(0.2)
# hubo.set_trace('blue')
#
# def turn_right():
#     for i in range(3):
#         hubo.turn_left()
#
# def turn_around():
#     for j in range(2):
#         hubo.turn_left()
#
# def move_to_wall():
#     while hubo.front_is_clear():
#         hubo.move()
#
#         while hubo.on_beeper():
#             hubo.pick_beeper()
#
# move_to_wall()
#
# turn_around()
# move_to_wall()
#
# turn_right()
# hubo.move()
#
# while hubo.carries_beepers():
#     hubo.drop_beeper()
#
# turn_around()
# hubo.move()



# #Return
#
# create_world(avenues=20,streets=20)
# hubo=Robot(orientation='W',avenue=15, street=12)
# hubo.set_pause(0.15)
# hubo.set_trace('blue')
#
# def turn_right():
#     for i in range(3):
#         hubo.turn_left()
#
# def move_to_wall():
#     while hubo.front_is_clear():
#         hubo.move()
#
# while not hubo.facing_north():
#     hubo.turn_left()
#
# hubo.turn_left()
# move_to_wall()
# hubo.turn_left()
# move_to_wall()


# #Smart ZigZag
#
# create_world(avenues=8, streets=15)
# hubo=Robot()
# hubo.set_pause(0.1)
# hubo.set_trace('blue')
#
#
# def turn_right():
#     for i in range(3):
#         hubo.turn_left()
#
# def move_to_wall():
#     while hubo.front_is_clear():
#         hubo.move()
#
# def round_trip():
#     move_to_wall()
#     turn_right()
#
#     if hubo.front_is_clear():
#         hubo.move()
#         turn_right()
#         move_to_wall()
#         hubo.turn_left()
#
#         if hubo.front_is_clear():
#             hubo.move()
#             hubo.turn_left()
#
# hubo.turn_left()
# while hubo.front_is_clear():
#     round_trip()



# #Harvest Even More
#
# load_world('worlds/harvest4.wld')
# hubo=Robot()
# hubo.set_pause(0.1)
# hubo.set_trace('blue')
#
#
# def turn_right():
#     for i in range(3):
#         hubo.turn_left()
#
# def pick_and_move():
#     hubo.move()
#     while hubo.on_beeper():
#         hubo.pick_beeper()
#
# def cycle1():
#     for j in range(5):
#         pick_and_move()
#
#     hubo.turn_left()
#     pick_and_move()
#     hubo.turn_left()
#
#     for l in range(5):
#         pick_and_move()
#
# pick_and_move()
# for k in range(3):
#     cycle1()
#
#     if k!=2:
#         turn_right()
#         pick_and_move()
#         turn_right()

#Rain

# load_world('worlds/rain1.wld')
# hubo = Robot(orientation='E', avenue=2, street=6, beepers=100)
# hubo.set_trace('blue')
# hubo.set_pause(0.1)
#
# def turn_right():
#     for i in range(3):
#         hubo.turn_left()
#
# def move_to_wall():
#     while hubo.front_is_clear():
#         if hubo.right_is_clear():
#             hubo.drop_beeper()
#             hubo.move()
#
#         else:
#             hubo.move()
#
# hubo.move()
# turn_right()
# hubo.move()
#
# for j in range(4):
#     move_to_wall()
#     hubo.turn_left()
#
# while not hubo.right_is_clear():
#     hubo.move()

#
# #Follow right wall
#
# load_world('worlds/maze.wld')
# hubo = Robot()
# hubo.set_trace('blue')
# hubo.set_pause(0.1)
#
# def turn_right():
#     for i in range(3):
#         hubo.turn_left()
#
# def turn_around():
#     hubo.turn_left()
#     hubo.turn_left()
#
# def follow_right_wall():
#     if hubo.right_is_clear():
#         turn_right()
#         hubo.move()
#
#     elif hubo.front_is_clear():
#         hubo.move()
#
#     else:
#         hubo.turn_left()
#
#
# while not hubo.on_beeper():
#     follow_right_wall()