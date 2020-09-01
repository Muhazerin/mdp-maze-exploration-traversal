robot_simulation = True

map_size = dict(
    height=20,
    width=15
)

map_cells = [[None for _ in range(map_size['width'])] for _ in range(map_size['height'])]

image_paths = dict(
    blue='images/blue.gif',
    gray='images/gray.gif',
    green='images/green.gif',
    light_blue='images/light_blue.gif',
    light_green='images/light_green.gif',
    pink='images/pink.gif',
    red='images/red.gif',
    yellow='images/yellow.gif'
)

robot_grid = dict(
    north=[['images/robot/north/front_left.gif',
            'images/robot/north/front_center.gif',
            'images/robot/north/front_right.gif'],
           ['images/robot/north/center_left.gif',
            'images/robot/north/center_center.gif',
            'images/robot/north/center_right.gif'],
           ['images/robot/north/back_left.gif',
            'images/robot/north/back_center.gif',
            'images/robot/north/back_right.gif']],
    east=[['images/robot/east/1.gif',
           'images/robot/east/2.gif',
           'images/robot/east/3.gif'],
          ['images/robot/east/4.gif',
           'images/robot/east/5.gif',
           'images/robot/east/6.gif'],
          ['images/robot/east/7.gif',
           'images/robot/east/8.gif',
           'images/robot/east/9.gif']],
    south=[['images/robot/south/1.gif',
            'images/robot/south/2.gif',
            'images/robot/south/3.gif'],
           ['images/robot/south/4.gif',
            'images/robot/south/5.gif',
            'images/robot/south/6.gif'],
           ['images/robot/south/7.gif',
            'images/robot/south/8.gif',
            'images/robot/south/9.gif']],
    west=[['images/robot/west/1.gif',
           'images/robot/west/2.gif',
           'images/robot/west/3.gif'],
          ['images/robot/west/4.gif',
           'images/robot/west/5.gif',
           'images/robot/west/6.gif'],
          ['images/robot/west/7.gif',
           'images/robot/west/8.gif',
           'images/robot/west/9.gif']],

)

sensor_range = dict(
    front_middle=3,
    front_left=3,
    front_right=3,
    left=3,
    right=5
)

# TODO: Distinguish between start , goal and obstacle. Robot cannot enter start/goal now because the areas are marked as wall
