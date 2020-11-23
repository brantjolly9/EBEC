# A turtle animation that draws a hexagonal spiral

# Import the turtle library
from turtle import *

# Turtle setup
setup(900,900)
shape('turtle')
color('green')
width('2')

# Iterate a hexagon with side lengths increasing by 5
for run in range(0, 180, 5):
    forward(run)
    left(60)

done()
