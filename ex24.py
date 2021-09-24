
def roof_maker(length):
    roof_element = ' ---'
    roof = ''
    n = 0
    while n < length:
        n += 1
        roof += roof_element
    return roof

def wall_maker(length):
    wall_element = '   |'
    wall = '|'
    n = 0
    while n < length:
        n += 1
        wall += wall_element
    return wall

def board_maker(length, height):
    print(roof_maker(length))
    n = 0
    while n < height:
        n += 1
        print(wall_maker(length))
        print(roof_maker(length))


length = int(input('length = '))
height = int(input('height = '))
board_maker(length, height)
