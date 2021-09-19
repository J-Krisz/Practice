s = "01000000X000X011X0X"

def pandemic(world):
    continents = world.split('X')
    infected = 0
    for continent in continents:
        if '1' in continent:
            infected += len(continent)
    return 'X'.join(continent.replace('0', '1'))

print(pandemic(s))
