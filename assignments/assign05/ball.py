from point import Point
from velocity import Velocity
import arcade
import random

class Ball:
    
    def __init__(self):
        self.center = Point()  # start of the ball
        self.velocity = Velocity() # random speed
        self.radius = 10
        self.color = (random.randint(0,225), random.randint(0,225), random.randint(0,225)) # random color
        
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, self.color)
        #arcade.draw_line(self.center.x, self.center.y, self.center.x - 5*self.velocity.dx, self.center.y - 5*self.velocity.dy, self.color, 3)
    
    def advance(self):
        # add velocity to change move the balls position
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
    
    def bounce_horizontal(self):
        # flip the sign of velocity in the x direction when the ball hits a veritcal wall
        self.velocity.dx = -1 * self.velocity.dx
    
    def bounce_vertical(self):
        # flip the sign of velocity in the y direction when the ball hits a horizontal wall
        self.velocity.dy = -1 * self.velocity.dy
    
    def restart(self):
        # respons the ball when it goes out of bounds.
        self.center.x = 10 # locked at 10 for x
        self.center.y = random.randint(30,270) # variable change in y
        self.velocity = Velocity() # random change in speed
        self.color = (random.randint(0,225), random.randint(0,225), random.randint(0,225)) # new color