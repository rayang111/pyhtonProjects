from turtle import *
import turtle

tl = turtle

n = 10
colore = ["maroon","red","blue","orange","pink","black","green"]
tl.hideturtle()
tracer(False)
tl.speed(0)
tl.pensize(4)
for i in range(0,5000):
    try:
        color(colore[i+1])
    except IndexError:
        colore = colore * 2
        color(colore[i+1])
    tl.down()
    tl.right(90)
    tl.forward(20+n)
    circle(n-i,n%(i+1))
    tl.right(50)
    n += 10
    if i%5 == 0:
        write("I wanna hold your hand")
