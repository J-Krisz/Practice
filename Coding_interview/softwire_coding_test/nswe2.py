# You are given an input string that controls the movement of a robot, each
# character instructing it to move one step north, south, east or west. E.G.
# "NW" moves the robot one step north and then one step west, or "SE" move the
# robot one step south and one step east.
# Write a function that counts the number of locations that the robot visits
# more than once, including possibly its starting point.
# You should ignore any characters that are not capital N, S, E, or W.

# For example:
# "NS" would return 1
# "WEWNES" would return 2
# "SxWxNxN" would return 0

#        N
#        |
#        |
# W------+------E
#        |
#        |
#        S

# N= y+1, S= y-1
# E= x+1, W= x-1

# (x=0, y=0) --N--> (x=0, y=1) --S--> (x=0, y=0)
# (x=0, y=0) --W--> (x=-1, y=0) --E--> (x=0, y=0) 


from collections import deque as queue


def valid_move(direction):

    output = str()
    moves = ['N', 'S', 'W', 'E']
    for move in direction:
        if move in moves:
            output += move

    return output


def is_border(i, j):
    pass


def track_moves(direction):
    
    x = 0
    x_axis = [0]
    y = 0
    y_axis = [0]

    for move in direction:
        if move == 'E':
            x += 1
            y = y
            x_axis.append(x)
            y_axis.append(y)
        elif move == 'W':
            x -= 1
            y = y
            x_axis.append(x)
            y_axis.append(y)
        elif move == 'N':
            x = x
            y += 1
            x_axis.append(x)
            y_axis.append(y)
        else:
            x = x
            y -= 1
            x_axis.append(x)
            y_axis.append(y)

    return list(zip(x_axis, y_axis))


def check_grid(direction):
    
    visited = list()

    grid_size = len(valid_move(direction))
    grid = [[(False) for x in range(grid_size)] for y in range(grid_size)]

    index = track_moves(direction)

    for i, row in enumerate(grid):
        for j, col in enumerate(row):




    return grid



first = 'NS'    # returns 1
second = 'WEWNES'   # returns 2
third = 'SxWxNxN'   #returns 0

clean = valid_move(first)
clean2 = valid_move(second)
clean3 = valid_move(third)

print(check_grid(second))

# print(track_moves(clean))
# print(track_moves(clean2))
# print(track_position(clean3))
