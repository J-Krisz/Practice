def track_moves(direction):
    
    x = 0
    x_axis = [0]
    y = 0
    y_axis = [0]

    for step, move in enumerate(direction):
        if not x_axis[step]:
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


  # is value 
