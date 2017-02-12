from turtle import *

#draws a star
def star(x):
    bgcolor('black')
    fillcolor('yellow')
    begin_fill()
    right(72)
    forward(x)
    left(72)
    forward(x)
    right(144)
    forward(x)
    left(72)
    forward(x)
    right(144)
    forward(x)
    left(72)
    forward(x)
    right(144)
    forward(x)
    left(72)
    forward(x)
    right(144)
    forward(x)
    left(72)
    forward(x)
    end_fill()

#draws a starry night
def starry_night():
    print """We are going to paint the sky with stars. Keep your star sizes
between 5 and 25 so we can see them."""
    sizes_of_stars = [(int(raw_input("Size of first star? "))),
    (int(raw_input("Size of second star? "))),
    (int(raw_input("Size of third star? "))),
    (int(raw_input("Size of fourth star? "))),
    (int(raw_input("Size of fifth star? "))),
    (int(raw_input("Size of sixth star? "))),
    (int(raw_input("Size of seventh star? "))),
    (int(raw_input("Size of eigth star? ")))]
    first, second, third, fourth, fifth, sixth, seventh, eigth = sizes_of_stars
    coord_list = [(-100, -100, first), (-200, -200, second), (200, -100, third),
    (-150, 75, fourth), (-300, 175, fifth), (45, 150, sixth), (150, 75, seventh),
    (-300, -75, eigth)]
    for coord in coord_list:
        up()
        home()
        x, y, size = coord
        setheading(270)
        forward(x)
        setheading(0)
        forward(y)
        down()
        star(size)

starry_night()
