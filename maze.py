from turtle import *

size = 900

setup(size,size)
bgpic('maze.png')
shape('turtle')
color('green')
width('7')

# Write your code here

speed(8)
color('green')
left(100)
circle(20, 75)
forward(27)

circle(-17, 90)
forward(10)
circle(15, 100)
forward(85)
circle(15, 450)
forward(20)
right(95)
forward(87)
left(90)
# forward(80)
for i in range(8):
    forward(10)
    dot(5)

right(90)
forward(83)
left(90)
forward(275)
right(90)
forward(40)
right(90)
forward(715)
right(90)
forward(760)
right(90)
forward(379)
left(90)
forward(30)

done()
