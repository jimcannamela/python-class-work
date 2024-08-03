from turtle import *
for steps in range(100):
    for c in ('blue', 'red', 'green','yellow','black','white'):
        color(c)
        forward(steps)
        right(30)