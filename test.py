import turtle
colors = ['red', 'yellow', 'purple', 'blue', 'green', 'orange'
]
a = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    a.pencolor(colors[x%6])
    a.width(x//100 + 1)
    a.forward(x)
    a.left(50)