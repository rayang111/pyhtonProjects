from turtle import *
import turtle
turtle.colormode(255)

tur = Turtle()

tur.hideturtle()


tur.speed(5)
tur.pensize(50)

n = 0

f =  [255,0,0]
for v in range(0,25):
    for w in f:
        
        f = list(f)
        if n == 1 and ( f[0] >= 255 and f[1] <= 0 and f[2] <= 0 ):
            n = 0

        if f[0] - 1 < 0 and f[1] + 1 > 255 and f[2] + 1 > 255:
            n = 1
        
        if n == 0 and ( f[0] > 0 and f[1] < 255 and f[2] < 255 ):
            f[0] = f[0] - 1
            f[1] = f[1] + 1
            f[2] = f[2] + 1
        else:
            n = 1
            
        if n == 1 and ( f[0] >= 0 and f[1] <= 255 and f[2] <= 255 ):
            f[0] = f[0] + 1
            f[1] = f[1] - 1
            f[2] = f[2] - 1




        print(f,n)

        f = tuple(f)
        
            

            

        
            
        tur.down()
        tur.pencolor(f)
        tur.forward(5)
        
        
