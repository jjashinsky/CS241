import arcade
import random
from point import Point
from velocity import Velocity
from globals import *

class FlyingObject:
    
    """
    This is a base class for all flying objects (bullets and targets)
    Most attributes are initially set for the bullet class
    """
    
    def __init__(self):
        self.center = Point() # starts at (0,0)
        self.velocity = Velocity() # randomly generated speed
        self.alive = True
        self.radius = BULLET_RADIUS
        self.color = BULLET_COLOR
    
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, self.color)
    
    # this will return false if the center is outside of the game screem
    def is_off_screen(self):
        if self.center.x > SCREEN_WIDTH or self.center.y < 0 or self.center.y > SCREEN_HEIGHT:
            return True
        
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy