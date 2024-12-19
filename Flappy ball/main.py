import pgzrun
from random import randint
HEIGHT = 600
WIDTH = 800
TITLE ='FLAPPY FLAP FLIPFLOP FLOPPIDY FLIP FLAP'
R = randint(0,255)
G = randint(0,255)
B = randint(0,255)
jump = randint(300,1000)
i = randint(1,2)
if i == 1:
    jump = jump*-1
CLR = R,G,B
GRAVITY = randint(1000,5000)

class Ball:
    def __init__(self,radius,x,y):
        self.radius = radius
        self.x = x
        self.y = y
        self.vx = randint(50,1000)
        self.vy = 0
    def bounce(self):
        pos = (self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,CLR)

ball = Ball(randint(10,100),100,100)
def draw():
    screen.clear()
    ball.bounce()
    

def update(dt):
    uy = ball.vy
    ball.vy += GRAVITY*dt
    ball.y += (uy+ball.vy)*0.5*dt
    if ball.y > HEIGHT-ball.radius:
        ball.y = HEIGHT-ball.radius
        ball.vy = -ball.vy*0.9
    ball.x += ball.vx*dt
    if ball.x > WIDTH - ball.radius or ball.x < 0 + ball.radius:
        ball.vx =- ball.vx

def on_key_down(key):
    if key == keys.SPACE:
        ball.vy = jump

pgzrun.go()